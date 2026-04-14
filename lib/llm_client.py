#!/usr/bin/env python3
"""
LLM Client - Large Language Model Client
Supports OpenAI-compatible APIs
"""

import os
import json
import time
import requests
from typing import Dict, List, Optional, Any


class LLMClient:
    """Large Language Model Client"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        # Default config
        self.api_key = self.config.get('apiKey') or os.getenv('LLM_API_KEY', '')
        self.base_url = self.config.get('baseUrl') or os.getenv('LLM_BASE_URL', 
            'https://api.openai.com/v1')
        self.model = self.config.get('model', 'gpt-4')
        self.max_tokens = self.config.get('maxTokens', 4096)
        self.temperature = self.config.get('temperature', 0.7)
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def chat(self, 
             messages: List[Dict[str, str]], 
             model: Optional[str] = None,
             temperature: Optional[float] = None,
             max_tokens: Optional[int] = None) -> Dict[str, Any]:
        """
        Send chat request
        
        Args:
            messages: Message list [{"role": "user", "content": "..."}]
            model: Model name
            temperature: Temperature parameter
            max_tokens: Max tokens
        
        Returns:
            API response
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model or self.model,
            "messages": messages,
            "temperature": temperature if temperature is not None else self.temperature,
            "max_tokens": max_tokens or self.max_tokens
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ LLM API call failed: {e}")
            return {"error": str(e)}
    
    def generate(self, 
                 prompt: str, 
                 system_prompt: Optional[str] = None,
                 **kwargs) -> str:
        """
        Simplified generation interface
        
        Args:
            prompt: User input
            system_prompt: System prompt
            **kwargs: Additional parameters
        
        Returns:
            Generated text
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        result = self.chat(messages, **kwargs)
        
        if "error" in result:
            return ""
        
        return result.get("choices", [{}])[0].get("message", {}).get("content", "")
    
    def stream_chat(self,
                    messages: List[Dict[str, str]],
                    model: Optional[str] = None,
                    temperature: Optional[float] = None,
                    max_tokens: Optional[int] = None):
        """
        Stream chat response
        
        Args:
            messages: Message list
            model: Model name
            temperature: Temperature
            max_tokens: Max tokens
        
        Yields:
            Response chunks
        """
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model or self.model,
            "messages": messages,
            "temperature": temperature if temperature is not None else self.temperature,
            "max_tokens": max_tokens or self.max_tokens,
            "stream": True
        }
        
        try:
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=120,
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    line = line.decode('utf-8')
                    if line.startswith('data: '):
                        data = line[6:]
                        if data != '[DONE]':
                            try:
                                chunk = json.loads(data)
                                content = chunk.get('choices', [{}])[0].get('delta', {}).get('content', '')
                                if content:
                                    yield content
                            except json.JSONDecodeError:
                                continue
                                
        except requests.exceptions.RequestException as e:
            print(f"❌ LLM API stream failed: {e}")
            yield f"Error: {str(e)}"


def get_llm_client(model_type: str = "openai", config: Optional[Dict] = None) -> LLMClient:
    """
    Get LLM client instance
    
    Args:
        model_type: Model type (openai, anthropic, etc.)
        config: Configuration
    
    Returns:
        LLM client instance
    """
    # Can extend to support different providers
    return LLMClient(config)


if __name__ == "__main__":
    # Test
    client = LLMClient()
    
    # Simple test
    result = client.generate("Hello, how are you?")
    print(f"Response: {result}")
