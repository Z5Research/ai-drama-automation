<h1 align="center">
  <br>
  <a href="https://github.com/Z5Research/ai-drama-automation">
    <img src="https://img.shields.io/badge/AI-Drama%20Automation-blue?style=for-the-badge&logo=video" alt="AI Drama Automation" width="300">
  </a>
  <br>
  AI Drama Automation
  <br>
</h1>

<p align="center">
  <a href="README_CN.md">🇨🇳 中文</a> •
  <a href="README_EN.md">🇺🇸 English</a>
</p>

<h4 align="center">One-liner to Complete AI Drama Video - End-to-End Automation Framework</h4>
<h4 align="center">一句话到完整AI漫剧 - 端到端自动化框架</h4>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </a>
  <a href="#features">
    <img src="https://img.shields.io/badge/version-2.0.0-green.svg" alt="Version">
  </a>
  <a href="#workflow">
    <img src="https://img.shields.io/badge/stages-7-blue.svg" alt="Stages">
  </a>
  <a href="#templates">
    <img src="https://img.shields.io/badge/templates-11-orange.svg" alt="Templates">
  </a>
</p>

<br>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#workflow">Workflow</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#templates">Templates</a> •
  <a href="#examples">Examples</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <b>AI漫剧自动化生成框架</b><br>
  从一句话创意到完整视频的全流程自动化解决方案<br>
  包含剧本解析、角色提取、场景分析、分镜生成、图像生成、视频生成、一致性控制
</p>

---

## Features | 核心特性

- 🎬 **End-to-End Automation** - 从创意到成片的完整自动化流程
- 🎭 **Character Consistency** - 跨镜头角色外观一致性控制
- 🎨 **Scene Coherence** - 场景风格统一性保证
- 📊 **Storyboard Generation** - 智能分镜提示词生成
- 🎥 **Multi-Model Integration** - LLM + 图像生成 + 视频生成
- 📝 **Professional Templates** - 专业模板和术语库

---

## Workflow | 工作流程

```
剧本解析 → 角色提取 → 场景分析 → 分镜生成 → 图像生成 → 视频生成 → 合成导出
    ↓           ↓           ↓           ↓           ↓           ↓           ↓
  Script    Character    Scene     Storyboard    Image       Video       Final
  Parsing   Extraction   Analysis  Generation  Generation  Generation   Export
```

### Stage 1: Script Parsing | 剧本解析

- 自动识别剧本格式
- 提取场次、场景描述、角色对白、动作指示
- NLP分析：情绪曲线、节奏变化
- 自动生成场次时长估算

### Stage 2: Character Extraction | 角色提取

- 基础外貌（年龄、性别、体型、五官特征）
- 发型发色、肤色
- 服装造型（支持多场次服装变化追踪）
- 角色气质/性格的视觉化表达
- 标志性道具/配饰

### Stage 3: Scene Analysis | 场景分析

- 场景类型（室内/室外、具体地点）
- 空间结构、关键道具布置
- 光线设计（光源类型、方向、强度、色温）
- 色彩基调、视觉氛围
- 天气/时间/季节

### Stage 4: Storyboard Generation | 分镜生成

- 镜头编号（场次-镜号）
- 景别（大特写/特写/中近景/中景/中远景/远景/大远景）
- 画面构图（三分法位置、视线引导）
- 角色动作、表情、站位
- 运镜方式（固定/推/拉/摇/移/跟等）
- 情绪氛围关键词
- 建议时长（秒）
- 转场方式

### Stage 5: Image Generation | 图像生成

- 关键帧图像生成
- 角色一致性控制（Seed锁定/IP-Adapter）
- 风格统一性保证

### Stage 6: Video Generation | 视频生成

- 图生视频（Image-to-Video）
- 运动幅度控制
- 帧率、分辨率设置
- 风格一致性配置

### Stage 7: Final Export | 合成导出

- 视频片段拼接
- 转场效果添加
- 音频合成（TTS配音+背景音乐）
- 字幕生成
- 最终渲染导出

---

## Quick Start | 快速开始

### Prerequisites | 前置要求

- Python 3.8+
- FFmpeg (视频处理)
- API Keys:
  - LLM API (OpenAI compatible)
  - Image Generation API
  - Video Generation API

### Installation | 安装

```bash
# Clone
git clone https://github.com/Z5Research/ai-drama-automation.git

# Install dependencies
cd ai-drama-automation
pip install -r requirements.txt

# Configure API keys
cp config/config.example.json config/config.json
# Edit config.json with your API keys
```

### Basic Usage | 基本使用

```python
from ai_drama import DramaPipeline

# Initialize
pipeline = DramaPipeline(config_path="config/config.json")

# Generate from one-liner
result = pipeline.generate(
    idea="一个年轻人在咖啡馆遇到多年未见的朋友",
    style="cinematic",
    duration=60  # seconds
)

# Output
print(result.video_path)
print(result.storyboard)
print(result.characters)
```

---

## Templates | 模板

### Character Template | 角色模板

```json
{
  "name": "角色名",
  "age": "年龄",
  "gender": "性别",
  "appearance": {
    "face": "五官特征",
    "hair": "发型发色",
    "skin": "肤色",
    "body": "体型"
  },
  "clothing": {
    "style": "服装风格",
    "color": "颜色搭配",
    "accessories": ["配饰"]
  },
  "personality": "性格气质关键词",
  "signature_items": ["标志性道具"]
}
```

### Scene Template | 场景模板

```json
{
  "location": "地点类型",
  "type": "室内/室外",
  "structure": "空间结构",
  "lighting": {
    "source": "光源类型",
    "direction": "方向",
    "intensity": "强度",
    "color_temp": "色温"
  },
  "color_palette": ["主色调"],
  "atmosphere": "氛围关键词",
  "weather": "天气",
  "time_of_day": "时间"
}
```

### Storyboard Template | 分镜模板

```json
{
  "shot_id": "场次-镜号",
  "shot_type": "景别",
  "composition": "构图描述",
  "characters": ["角色动作"],
  "camera_movement": "运镜方式",
  "mood": "情绪氛围",
  "duration": 5,
  "transition": "转场方式"
}
```

---

## Examples | 示例

### Example 1: Simple Scene | 简单场景

**Input**:
```
一个年轻女孩在雨中的街道上奔跑
```

**Output**:
- Character: 年轻女孩、白裙、长发
- Scene: 雨天街道、灰蓝色调
- Storyboard: 5个镜头
- Video: 15秒

### Example 2: Complex Narrative | 复杂叙事

**Input**:
```
一个创业者从失败到成功的故事
```

**Output**:
- Characters: 主角、配角3人
- Scenes: 办公室、咖啡馆、发布会现场
- Storyboard: 12个镜头
- Video: 60秒

---

## Documentation | 文档

- **[Workflow Guide](docs/workflow.md)** - 完整工作流程说明
- **[Character Extraction](docs/character_extraction.md)** - 角色提取方法论
- **[Scene Analysis](docs/scene_analysis.md)** - 场景分析指南
- **[Storyboard Generation](docs/storyboard_generation.md)** - 分镜生成详解
- **[Consistency Control](docs/consistency_control.md)** - 一致性控制策略
- **[API Integration](docs/api_integration.md)** - API集成指南

---

## References | 参考资料

- **[Shot Terminology](references/shot_terminology.md)** - 镜头术语库
- **[Mood Keywords](references/mood_keywords.md)** - 情绪关键词库
- **[Visual Style Library](references/visual_styles.md)** - 视觉风格库

---

## Output | 输出内容

| 产出项 | 格式 | 说明 |
|--------|------|------|
| 角色设定文档 | JSON + Markdown | 外貌、服装、气质关键词、生图提示词 |
| 场景设定文档 | JSON + Markdown | 空间描述、光线、色调、氛围词 |
| 分镜提示词表 | CSV + JSON | 按幕/场景/镜头三级结构组织 |
| 一致性检查报告 | Markdown | 角色/场景偏差标注 + 修复建议 |
| 完整视频 | MP4 | 合成后的最终视频 |

---

## Architecture | 架构设计

```
ai-drama-automation/
├── scripts/              # 核心脚本
│   ├── parse_script.py      # 剧本解析
│   ├── character_extractor.py  # 角色提取
│   ├── scene_analyzer.py    # 场景分析
│   ├── storyboard_generator.py  # 分镜生成
│   ├── image_generator.py   # 图像生成
│   ├── video_generator.py   # 视频生成
│   └── compose_export.py    # 合成导出
├── config/               # 配置文件
│   ├── config.json          # 主配置
│   └── prompts/             # 提示词模板
├── templates/            # 输出模板
├── references/           # 参考资料
│   ├── shot_terminology.md  # 镜头术语
│   ├── mood_keywords.md     # 情绪关键词
│   └── visual_styles.md     # 视觉风格
└── examples/             # 示例
```

---

## License | 许可证

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

---

<p align="center">
  Built with ❤️ for AI content creators
</p>

<p align="center">
  <a href="https://github.com/Z5Research/ai-drama-automation">
    <img src="https://img.shields.io/github/stars/Z5Research/ai-drama-automation?style=social" alt="Stars">
  </a>
  <a href="https://github.com/Z5Research/ai-drama-automation/issues">
    <img src="https://img.shields.io/github/issues/Z5Research/ai-drama-automation" alt="Issues">
  </a>
</p>