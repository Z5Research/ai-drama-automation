#!/usr/bin/env python3
"""
AI Drama Automation Pipeline
Generate complete drama video from one-liner idea
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime
from typing import Dict, List, Optional

# Add lib to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from llm_client import get_llm_client
from api_client import DramaAPIClient, ImageGenerator, VideoGenerator


class DramaPipeline:
    """AI Drama Automation Pipeline"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or self._load_config()
        
        # Initialize clients
        self.llm = get_llm_client(
            model_type=self.config.get('llmType', 'openai'),
            config=self.config.get('llmConfig', {})
        )
        
        self.api = DramaAPIClient(self.config.get('apiConfig', {}))
        self.image_gen = ImageGenerator(self.config.get('imageConfig', {}))
        self.video_gen = VideoGenerator(self.config.get('videoConfig', {}))
        
        # State tracking
        self.project_id = None
        self.current_step = None
        self.logs = []
    
    def _load_config(self) -> Dict:
        """Load configuration"""
        config_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'config',
            'config.json'
        )
        
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Default config
        return {
            "model": "your-llm-model",
            "imageModel": "your-image-model",
            "videoModel": "your-video-model",
            "style": "cinematic",
            "aspectRatio": "9:16",
            "maxRetries": 3,
            "timeout": 300
        }
    
    def _log(self, message: str, level: str = "INFO"):
        """Log message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def _load_prompt(self, prompt_name: str) -> str:
        """Load prompt template"""
        prompt_path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'config',
            'prompts',
            f'{prompt_name}.md'
        )
        
        if os.path.exists(prompt_path):
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        
        return ""
    
    # ==================== Step 1: Script Generation ====================
    
    def generate_script(self, idea: str, episodes: int = 1, style: str = "cinematic") -> Dict:
        """
        Generate script from idea
        
        Args:
            idea: Creative description
            episodes: Number of episodes
            style: Visual style
        
        Returns:
            Generated script data
        """
        self._log(f"Generating script from idea: {idea}")
        self.current_step = "script_generation"
        
        # Load prompt template
        prompt_template = self._load_prompt('script_prompt')
        
        # Build prompt
        prompt = prompt_template.format(
            idea=idea,
            episodes=episodes,
            style=style
        )
        
        # Call LLM
        result = self.llm.chat(prompt)
        
        # Parse result
        script_data = self._parse_script_result(result)
        
        # Create project
        self.project_id = self.api.create_project(script_data)
        
        self._log(f"Script generated: {len(script_data.get('scenes', []))} scenes")
        
        return script_data
    
    def _parse_script_result(self, result: str) -> Dict:
        """Parse script result from LLM"""
        try:
            # Try to extract JSON
            import re
            json_match = re.search(r'\{.*\}', result, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        
        # Return structured data
        return {
            "title": "Generated Drama",
            "scenes": [
                {
                    "scene_id": 1,
                    "description": result[:500],
                    "characters": [],
                    "dialogue": [],
                    "actions": []
                }
            ]
        }
    
    # ==================== Step 2: Character Extraction ====================
    
    def extract_characters(self, script_data: Dict) -> List[Dict]:
        """
        Extract characters from script
        
        Args:
            script_data: Script data
        
        Returns:
            List of character profiles
        """
        self._log("Extracting characters from script")
        self.current_step = "character_extraction"
        
        # Load prompt template
        prompt_template = self._load_prompt('character_prompt')
        
        # Build prompt
        prompt = prompt_template.format(
            script=json.dumps(script_data, ensure_ascii=False, indent=2)
        )
        
        # Call LLM
        result = self.llm.chat(prompt)
        
        # Parse characters
        characters = self._parse_characters_result(result)
        
        # Save to project
        for char in characters:
            self.api.create_character(self.project_id, char)
        
        self._log(f"Extracted {len(characters)} characters")
        
        return characters
    
    def _parse_characters_result(self, result: str) -> List[Dict]:
        """Parse character extraction result"""
        try:
            import re
            json_match = re.search(r'\[.*\]', result, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        
        return []
    
    # ==================== Step 3: Scene Analysis ====================
    
    def analyze_scenes(self, script_data: Dict) -> List[Dict]:
        """
        Analyze scenes from script
        
        Args:
            script_data: Script data
        
        Returns:
            List of scene descriptions
        """
        self._log("Analyzing scenes")
        self.current_step = "scene_analysis"
        
        scenes = []
        
        for scene in script_data.get('scenes', []):
            # Analyze scene
            scene_data = self._analyze_single_scene(scene)
            scenes.append(scene_data)
            
            # Save to project
            self.api.create_scene(self.project_id, scene_data)
        
        self._log(f"Analyzed {len(scenes)} scenes")
        
        return scenes
    
    def _analyze_single_scene(self, scene: Dict) -> Dict:
        """Analyze single scene"""
        return {
            "scene_id": scene.get('scene_id'),
            "location": scene.get('location', 'Unknown'),
            "type": "indoor" if "室内" in scene.get('description', '') else "outdoor",
            "lighting": {
                "source": "natural",
                "intensity": "soft",
                "color_temp": "warm"
            },
            "atmosphere": scene.get('mood', 'neutral'),
            "color_palette": ["default"]
        }
    
    # ==================== Step 4: Storyboard Generation ====================
    
    def generate_storyboard(self, script_data: Dict, characters: List[Dict], scenes: List[Dict]) -> List[Dict]:
        """
        Generate storyboard
        
        Args:
            script_data: Script data
            characters: Character profiles
            scenes: Scene descriptions
        
        Returns:
            List of storyboard shots
        """
        self._log("Generating storyboard")
        self.current_step = "storyboard_generation"
        
        # Load prompt template
        prompt_template = self._load_prompt('storyboard_prompt')
        
        # Build prompt
        prompt = prompt_template.format(
            script=json.dumps(script_data, ensure_ascii=False, indent=2),
            characters=json.dumps(characters, ensure_ascii=False, indent=2),
            scenes=json.dumps(scenes, ensure_ascii=False, indent=2)
        )
        
        # Call LLM
        result = self.llm.chat(prompt)
        
        # Parse storyboard
        storyboard = self._parse_storyboard_result(result)
        
        # Save to project
        for shot in storyboard:
            self.api.create_shot(self.project_id, shot)
        
        self._log(f"Generated {len(storyboard)} shots")
        
        return storyboard
    
    def _parse_storyboard_result(self, result: str) -> List[Dict]:
        """Parse storyboard result"""
        try:
            import re
            json_match = re.search(r'\[.*\]', result, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        
        return []
    
    # ==================== Step 5: Image Generation ====================
    
    def generate_images(self, storyboard: List[Dict], characters: List[Dict]) -> List[str]:
        """
        Generate keyframe images
        
        Args:
            storyboard: Storyboard shots
            characters: Character profiles
        
        Returns:
            List of image paths
        """
        self._log("Generating keyframe images")
        self.current_step = "image_generation"
        
        image_paths = []
        
        for i, shot in enumerate(storyboard):
            # Build prompt
            prompt = self._build_image_prompt(shot, characters)
            
            # Generate image
            image_path = self.image_gen.generate(
                prompt=prompt,
                style=self.config.get('style', 'cinematic'),
                aspect_ratio=self.config.get('aspectRatio', '9:16')
            )
            
            if image_path:
                image_paths.append(image_path)
                self._log(f"Generated image {i+1}/{len(storyboard)}")
        
        return image_paths
    
    def _build_image_prompt(self, shot: Dict, characters: List[Dict]) -> str:
        """Build image generation prompt"""
        parts = []
        
        # Scene description
        parts.append(f"Scene: {shot.get('composition', '')}")
        
        # Characters
        for char_name in shot.get('characters', []):
            char = next((c for c in characters if c.get('name') == char_name), None)
            if char:
                parts.append(f"Character: {char.get('appearance', '')}")
        
        # Camera
        parts.append(f"Camera: {shot.get('shot_type', '')} {shot.get('camera_movement', '')}")
        
        # Mood
        parts.append(f"Mood: {shot.get('mood', '')}")
        
        return ", ".join(parts)
    
    # ==================== Step 6: Video Generation ====================
    
    def generate_videos(self, image_paths: List[str], storyboard: List[Dict]) -> List[str]:
        """
        Generate video clips from images
        
        Args:
            image_paths: Image paths
            storyboard: Storyboard shots
        
        Returns:
            List of video paths
        """
        self._log("Generating video clips")
        self.current_step = "video_generation"
        
        video_paths = []
        
        for i, (image_path, shot) in enumerate(zip(image_paths, storyboard)):
            # Generate video
            video_path = self.video_gen.generate_from_image(
                image_path=image_path,
                duration=shot.get('duration', 5),
                motion_strength="medium"
            )
            
            if video_path:
                video_paths.append(video_path)
                self._log(f"Generated video {i+1}/{len(image_paths)}")
        
        return video_paths
    
    # ==================== Step 7: Final Export ====================
    
    def export_video(self, video_paths: List[str], output_path: str = "output.mp4") -> str:
        """
        Export final video
        
        Args:
            video_paths: Video clip paths
            output_path: Output path
        
        Returns:
            Final video path
        """
        self._log("Exporting final video")
        self.current_step = "final_export"
        
        # Concatenate videos
        final_path = self._concatenate_videos(video_paths, output_path)
        
        self._log(f"Final video exported: {final_path}")
        
        return final_path
    
    def _concatenate_videos(self, video_paths: List[str], output_path: str) -> str:
        """Concatenate video clips"""
        import subprocess
        
        # Create file list
        list_file = "/tmp/video_list.txt"
        with open(list_file, 'w') as f:
            for path in video_paths:
                f.write(f"file '{path}'\n")
        
        # Use FFmpeg to concatenate
        cmd = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", list_file,
            "-c", "copy",
            output_path
        ]
        
        subprocess.run(cmd, check=True)
        
        return output_path
    
    # ==================== Full Pipeline ====================
    
    def run(self, idea: str, episodes: int = 1, style: str = "cinematic") -> Dict:
        """
        Run full pipeline
        
        Args:
            idea: Creative idea
            episodes: Number of episodes
            style: Visual style
        
        Returns:
            Result data
        """
        self._log(f"Starting full pipeline for: {idea}")
        
        try:
            # Step 1: Generate script
            script_data = self.generate_script(idea, episodes, style)
            
            # Step 2: Extract characters
            characters = self.extract_characters(script_data)
            
            # Step 3: Analyze scenes
            scenes = self.analyze_scenes(script_data)
            
            # Step 4: Generate storyboard
            storyboard = self.generate_storyboard(script_data, characters, scenes)
            
            # Step 5: Generate images
            image_paths = self.generate_images(storyboard, characters)
            
            # Step 6: Generate videos
            video_paths = self.generate_videos(image_paths, storyboard)
            
            # Step 7: Export final video
            final_video = self.export_video(video_paths)
            
            return {
                "success": True,
                "project_id": self.project_id,
                "script": script_data,
                "characters": characters,
                "scenes": scenes,
                "storyboard": storyboard,
                "image_paths": image_paths,
                "video_paths": video_paths,
                "final_video": final_video,
                "logs": self.logs
            }
            
        except Exception as e:
            self._log(f"Pipeline failed: {str(e)}", level="ERROR")
            return {
                "success": False,
                "error": str(e),
                "logs": self.logs
            }


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="AI Drama Automation Pipeline")
    parser.add_argument("--idea", required=True, help="Creative idea")
    parser.add_argument("--episodes", type=int, default=1, help="Number of episodes")
    parser.add_argument("--style", default="cinematic", help="Visual style")
    parser.add_argument("--output", default="output.mp4", help="Output video path")
    parser.add_argument("--config", help="Config file path")
    
    args = parser.parse_args()
    
    # Load config
    config = None
    if args.config:
        with open(args.config, 'r') as f:
            config = json.load(f)
    
    # Create pipeline
    pipeline = DramaPipeline(config)
    
    # Run
    result = pipeline.run(
        idea=args.idea,
        episodes=args.episodes,
        style=args.style
    )
    
    # Print result
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    return 0 if result.get('success') else 1


if __name__ == "__main__":
    sys.exit(main())
