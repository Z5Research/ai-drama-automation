# AI Drama Automation - English Documentation

**End-to-End AI Drama Video Generation Framework - From One-Liner to Complete Video**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](version)

---

## 📋 Overview

Intelligently transform a one-liner idea into a complete AI drama video with full automation support.

### Core Pipeline

```
Script Parsing → Character Extraction → Scene Analysis → Storyboard Generation → Image Generation → Video Generation → Final Export
```

---

## 🎯 Key Features

### 1. End-to-End Automation

- **Input**: One-liner idea or complete script
- **Output**: Complete video + all intermediate artifacts
- **Pipeline**: 7-stage fully automated processing

### 2. Character Consistency Control

- **Appearance Consistency**: Maintain character appearance across shots
- **Costume Tracking**: Multi-scene costume change management
- **Personality Unity**: Visual expression of character traits

### 3. Scene Coherence Guarantee

- **Style Unity**: Consistent scene style across shots
- **Lighting Design**: Complete lighting plan
- **Color Palette**: Unified visual atmosphere

### 4. Intelligent Storyboard Generation

- **Professional Terminology**: Standard shot language
- **Mood Keywords**: Rich emotional expressions
- **Composition Guide**: Professional visual design

---

## 🔄 Workflow Details

### Stage 1: Script Parsing

**Functions**:
- Auto-identify script format
- Extract scenes, descriptions, dialogues, actions
- NLP analysis: emotion curves, rhythm changes
- Auto-generate scene duration estimates

**Output**:
```json
{
  "scenes": [
    {
      "scene_id": 1,
      "location": "Coffee Shop",
      "time": "Afternoon",
      "characters": ["Alex", "Emma"],
      "dialogue": [...],
      "actions": [...],
      "mood": "Casual and pleasant",
      "duration": 15
    }
  ]
}
```

### Stage 2: Character Extraction

**Extracted Content**:
- Basic appearance (age, gender, body type, facial features)
- Hair style and color, skin tone
- Costume design (multi-scene costume tracking)
- Visual expression of personality/temperament
- Signature props/accessories

**Output Format**:
```json
{
  "name": "Alex",
  "age": "25",
  "gender": "Male",
  "appearance": {
    "face": "Refined features, gentle eyes",
    "hair": "Black short hair, slight bangs",
    "skin": "Healthy wheat color",
    "body": "Well-proportioned"
  },
  "clothing": {
    "scene_1": "White shirt, jeans",
    "scene_2": "Dark suit, tie"
  },
  "personality": "Gentle, introverted, responsible",
  "signature_items": ["Glasses"]
}
```

### Stage 3: Scene Analysis

**Analysis Dimensions**:
- Scene type (indoor/outdoor, specific location)
- Spatial structure, key prop placement
- Lighting design (source, direction, intensity, color temperature)
- Color palette, visual atmosphere
- Weather/time/season

**Output Format**:
```json
{
  "location": "Coffee Shop",
  "type": "Indoor",
  "structure": "Open space, window seating, bar counter",
  "lighting": {
    "source": "Natural light + warm lighting",
    "direction": "Side light",
    "intensity": "Soft",
    "color_temp": "Warm tone"
  },
  "color_palette": ["Brown", "Beige", "Warm Yellow"],
  "atmosphere": "Cozy, comfortable, artistic",
  "props": ["Wooden tables", "Coffee cups", "Bookshelf"]
}
```

### Stage 4: Storyboard Generation

**Storyboard Content**:
- Shot ID (scene-shot number)
- Shot type (ECU/CU/MCU/MS/MLS/LS/ELS)
- Composition (rule of thirds, gaze direction)
- Character actions, expressions, positioning
- Camera movement (static/dolly in/dolly out/pan/truck/follow)
- Mood keywords
- Suggested duration (seconds)
- Transition type

**Output Format**:
```json
{
  "shot_id": "1-01",
  "shot_type": "Medium Shot",
  "composition": "Rule of thirds, protagonist at right third",
  "characters": [
    {
      "name": "Alex",
      "action": "Sitting by window, checking phone",
      "expression": "Focused",
      "position": "Right side of frame"
    }
  ],
  "camera_movement": "Static shot",
  "mood": "Quiet, expectant",
  "duration": 3,
  "transition": "Cut"
}
```

### Stage 5: Image Generation

**Generation Strategy**:
- Keyframe image generation
- Character consistency control (Seed locking/IP-Adapter)
- Style unity guarantee

**Parameters**:
```json
{
  "model": "text-to-image-model",
  "prompt": "Detailed scene and character description",
  "negative_prompt": "Elements to avoid",
  "style": "cinematic",
  "resolution": "1080P",
  "aspect_ratio": "9:16",
  "seed": 12345
}
```

### Stage 6: Video Generation

**Generation Method**:
- Image-to-Video
- Motion strength control
- Frame rate, resolution settings
- Style consistency configuration

**Parameters**:
```json
{
  "model": "image-to-video-model",
  "duration": 5,
  "frame_rate": 24,
  "motion_strength": "medium",
  "style_consistency": "high"
}
```

### Stage 7: Final Export

**Composition Process**:
1. Video clip concatenation
2. Transition effects
3. Audio synthesis (TTS dubbing + background music)
4. Subtitle generation
5. Final render export

**Output Configuration**:
```json
{
  "resolution": "1080P",
  "frame_rate": 24,
  "codec": "H.264",
  "audio_codec": "AAC",
  "subtitle_format": "SRT"
}
```

---

## 📥 User Input

**Required**:
- Creative description (one-liner or complete script)

**Optional**:
- Style reference images
- Character reference images
- Target aspect ratio
- Target duration
- Visual style keywords

---

## 📤 Final Output

| Output Item | Format | Description |
|-------------|--------|-------------|
| Character Design Doc | JSON + Markdown | Appearance, costume, personality keywords, generation prompts |
| Scene Design Doc | JSON + Markdown | Space description, lighting, color tone, atmosphere keywords |
| Storyboard Prompt Table | CSV + JSON | Organized by act/scene/shot hierarchy |
| Consistency Check Report | Markdown | Character/scene deviation notes + fix suggestions |
| Complete Video | MP4 | Final composed video |

---

## 🎨 Style Control

### Visual Styles

- **Cinematic**: Professional film quality
- **Anime**: 2D animation style
- **Realistic**: Highly realistic imagery
- **Artistic**: Artistic painting style

### Mood Atmosphere

- Positive/Negative
- Warm/Cold
- Tense/Relaxed
- Happy/Sad

---

## 🔧 Consistency Control Strategies

### Character Consistency

1. **Seed Locking**: Use fixed seed for generation
2. **IP-Adapter**: Reference image adaptation
3. **Feature Anchors**: Fixed key appearance features
4. **Costume Tracking**: Cross-scene costume management

### Scene Consistency

1. **Style Anchors**: Unified scene style
2. **Color Palette**: Fixed dominant colors
3. **Lighting Design**: Consistent light source parameters
4. **Spatial Structure**: Fixed scene layout

---

## 📚 Professional Terminology

### Shot Types

| Shot Type | Abbreviation | Characteristics |
|-----------|--------------|-----------------|
| Extreme Close-Up | ECU | Extreme close distance, emphasize details |
| Close-Up | CU | Face or object close-up |
| Medium Close-Up | MCU | Above chest |
| Medium Shot | MS | Above waist |
| Medium Long Shot | MLS | Above knees |
| Long Shot | LS | Full body or scene |
| Extreme Long Shot | ELS | Large-scale scene |

### Camera Movements

| Movement | English | Effect |
|----------|---------|--------|
| Static | Static | Still image |
| Dolly In | Dolly In | Visual approach |
| Dolly Out | Dolly Out | Visual retreat |
| Pan | Pan | Horizontal rotation |
| Truck | Truck | Horizontal movement |
| Follow | Follow | Follow subject |

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/Z5Research/ai-drama-automation.git
cd ai-drama-automation
pip install -r requirements.txt
```

### Configuration

```bash
cp config/config.example.json config/config.json
# Edit config.json with your API keys
```

### Usage

```python
from ai_drama import DramaPipeline

pipeline = DramaPipeline(config_path="config/config.json")

result = pipeline.generate(
    idea="A young person meets an old friend at a coffee shop",
    style="cinematic",
    duration=60
)

print(f"Video generated: {result.video_path}")
```

---

## 📄 License

MIT License

Copyright (c) 2026

---

**Built with ❤️ for AI content creators**