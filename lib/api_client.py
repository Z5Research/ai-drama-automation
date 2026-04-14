#!/usr/bin/env python3
"""
API Client - AI Drama Backend Client
"""

import os
import json
import time
import requests
from typing import Dict, List, Optional, Any


class DramaAPIClient:
    """AI Drama API Client"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        # API config
        self.base_url = self.config.get('apiUrl') or os.getenv('DRAMA_API_URL', 'http://localhost:3000')
        self.api_token = self.config.get('apiToken') or os.getenv('DRAMA_API_TOKEN', '')
        
        self.headers = {
            'Content-Type': 'application/json'
        }
        
        if self.api_token:
            self.headers['Authorization'] = f'Bearer {self.api_token}'
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Send API request"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers, timeout=30)
            elif method == 'POST':
                response = requests.post(url, headers=self.headers, json=data, timeout=60)
            elif method == 'PUT':
                response = requests.put(url, headers=self.headers, json=data, timeout=30)
            elif method == 'DELETE':
                response = requests.delete(url, headers=self.headers, timeout=30)
            else:
                return {"error": f"Unsupported method: {method}"}
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API request failed [{method} {endpoint}]: {e}")
            return {"error": str(e)}
    
    # ==================== Project Management ====================
    
    def create_project(self, title: str, description: str = "", **kwargs) -> Dict:
        """Create project"""
        data = {
            "title": title,
            "description": description,
            "status": kwargs.get("status", "draft"),
            "videoRatio": kwargs.get("videoRatio", "9:16"),
            "aiModel": kwargs.get("aiModel", "default")
        }
        return self._request('POST', '/api/projects', data)
    
    def get_project(self, project_id: str) -> Dict:
        """Get project details"""
        return self._request('GET', f'/api/projects/{project_id}')
    
    def list_projects(self, status: Optional[str] = None) -> Dict:
        """List projects"""
        endpoint = '/api/projects'
        if status:
            endpoint += f'?status={status}'
        return self._request('GET', endpoint)
    
    # ==================== Script Management ====================
    
    def create_script(self, project_id: str, content: str, **kwargs) -> Dict:
        """Create script"""
        data = {
            "projectId": project_id,
            "content": content,
            "title": kwargs.get("title", ""),
            "type": kwargs.get("type", "main")
        }
        return self._request('POST', '/api/scripts', data)
    
    # ==================== Character Management ====================
    
    def create_character(self, project_id: str, character: Dict) -> Dict:
        """Create character"""
        data = {
            "projectId": project_id,
            **character
        }
        return self._request('POST', '/api/characters', data)
    
    def get_characters(self, project_id: str) -> Dict:
        """Get project characters"""
        return self._request('GET', f'/api/projects/{project_id}/characters')
    
    # ==================== Scene Management ====================
    
    def create_scene(self, project_id: str, scene: Dict) -> Dict:
        """Create scene"""
        data = {
            "projectId": project_id,
            **scene
        }
        return self._request('POST', '/api/scenes', data)
    
    # ==================== Shot Management ====================
    
    def create_shot(self, project_id: str, shot: Dict) -> Dict:
        """Create shot"""
        data = {
            "projectId": project_id,
            **shot
        }
        return self._request('POST', '/api/shots', data)


class ImageGenerator:
    """Image Generation Client"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        self.api_key = self.config.get('apiKey') or os.getenv('IMAGE_API_KEY', '')
        self.api_url = self.config.get('apiUrl') or os.getenv('IMAGE_API_URL', '')
        self.model = self.config.get('model', 'default-model')
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def generate(self, 
                 prompt: str, 
                 style: str = "cinematic",
                 aspect_ratio: str = "9:16",
                 **kwargs) -> Optional[str]:
        """
        Generate image from prompt
        
        Args:
            prompt: Image description
            style: Visual style
            aspect_ratio: Aspect ratio
            **kwargs: Additional parameters
        
        Returns:
            Image path or URL
        """
        payload = {
            "model": self.model,
            "prompt": prompt,
            "style": style,
            "aspect_ratio": aspect_ratio,
            **kwargs
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            
            # Return image URL or path
            return result.get("data", [{}])[0].get("url") or result.get("image_path")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Image generation failed: {e}")
            return None


class VideoGenerator:
    """Video Generation Client"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        self.api_key = self.config.get('apiKey') or os.getenv('VIDEO_API_KEY', '')
        self.api_url = self.config.get('apiUrl') or os.getenv('VIDEO_API_URL', '')
        self.model = self.config.get('model', 'default-model')
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def generate_from_image(self,
                            image_path: str,
                            duration: int = 5,
                            motion_strength: str = "medium",
                            **kwargs) -> Optional[str]:
        """
        Generate video from image
        
        Args:
            image_path: Source image path or URL
            duration: Video duration in seconds
            motion_strength: Motion strength (low/medium/high)
            **kwargs: Additional parameters
        
        Returns:
            Video path or URL
        """
        payload = {
            "model": self.model,
            "image": image_path,
            "duration": duration,
            "motion_strength": motion_strength,
            **kwargs
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            result = response.json()
            
            # Return video URL or path
            return result.get("data", [{}])[0].get("url") or result.get("video_path")
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Video generation failed: {e}")
            return None


if __name__ == "__main__":
    # Test
    client = DramaAPIClient()
    print("API Client initialized")
    
    img_gen = ImageGenerator()
    print("Image Generator initialized")
    
    vid_gen = VideoGenerator()
    print("Video Generator initialized")
