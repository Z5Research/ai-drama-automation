# AI Drama Automation - 中文文档

**AI漫剧自动化生成框架 - 从一句话到完整视频**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](version)

---

## 📋 概述

将一句话创意智能转化为完整AI漫剧，支持全流程自动化处理。

### 核心流程

```
剧本解析 → 角色提取 → 场景分析 → 分镜生成 → 图像生成 → 视频生成 → 合成导出
```

---

## 🎯 核心特性

### 1. 端到端自动化

- **输入**: 一句话创意或完整剧本
- **输出**: 完整视频 + 所有中间产物
- **流程**: 7个阶段全自动处理

### 2. 角色一致性控制

- **外貌一致性**: 跨镜头角色外观保持
- **服装追踪**: 多场次服装变化管理
- **气质统一**: 性格视觉化表达

### 3. 场景连贯性保证

- **风格统一**: 场景风格跨镜头一致
- **光线设计**: 完整的光影方案
- **色彩基调**: 统一的视觉氛围

### 4. 智能分镜生成

- **专业术语库**: 标准镜头语言
- **情绪关键词**: 丰富的情感表达
- **构图指导**: 专业的画面设计

---

## 🔄 工作流程详解

### 阶段1: 剧本智能解析

**功能**:
- 自动识别剧本格式
- 提取场次、场景描述、角色对白、动作指示
- NLP分析：情绪曲线、节奏变化
- 自动生成场次时长估算

**输出**:
```json
{
  "scenes": [
    {
      "scene_id": 1,
      "location": "咖啡馆",
      "time": "下午",
      "characters": ["小明", "小红"],
      "dialogue": [...],
      "actions": [...],
      "mood": "轻松愉快",
      "duration": 15
    }
  ]
}
```

### 阶段2: 角色设定提取

**提取内容**:
- 基础外貌（年龄、性别、体型、五官特征）
- 发型发色、肤色
- 服装造型（支持多场次服装变化追踪）
- 角色气质/性格的视觉化表达
- 标志性道具/配饰

**输出格式**:
```json
{
  "name": "小明",
  "age": "25岁",
  "gender": "男",
  "appearance": {
    "face": "清秀五官、眼神温和",
    "hair": "黑色短发、略带刘海",
    "skin": "健康小麦色",
    "body": "身材匀称"
  },
  "clothing": {
    "scene_1": "白色衬衫、牛仔裤",
    "scene_2": "深色西装、领带"
  },
  "personality": "温和、内敛、有担当",
  "signature_items": ["眼镜"]
}
```

### 阶段3: 场景设定分析

**分析维度**:
- 场景类型（室内/室外、具体地点）
- 空间结构、关键道具布置
- 光线设计（光源类型、方向、强度、色温）
- 色彩基调、视觉氛围
- 天气/时间/季节

**输出格式**:
```json
{
  "location": "咖啡馆",
  "type": "室内",
  "structure": "开放式空间、靠窗座位区、吧台",
  "lighting": {
    "source": "自然光+暖色灯光",
    "direction": "侧面光",
    "intensity": "柔和",
    "color_temp": "暖色调"
  },
  "color_palette": ["棕色", "米色", "暖黄色"],
  "atmosphere": "温馨、舒适、文艺",
  "props": ["木质桌椅", "咖啡杯", "书架"]
}
```

### 阶段4: 分镜提示词生成

**分镜内容**:
- 镜头编号（场次-镜号）
- 景别（大特写/特写/中近景/中景/中远景/远景/大远景）
- 画面构图（三分法位置、视线引导）
- 角色动作、表情、站位
- 运镜方式（固定/推/拉/摇/移/跟等）
- 情绪氛围关键词
- 建议时长（秒）
- 转场方式

**输出格式**:
```json
{
  "shot_id": "1-01",
  "shot_type": "中景",
  "composition": "三分法、主角位于右侧三分之一",
  "characters": [
    {
      "name": "小明",
      "action": "坐在窗边看手机",
      "expression": "专注",
      "position": "画面右侧"
    }
  ],
  "camera_movement": "固定镜头",
  "mood": "安静、期待",
  "duration": 3,
  "transition": "硬切"
}
```

### 阶段5: 图像生成

**生成策略**:
- 关键帧图像生成
- 角色一致性控制（Seed锁定/IP-Adapter）
- 风格统一性保证

**参数配置**:
```json
{
  "model": "text-to-image-model",
  "prompt": "详细的场景和角色描述",
  "negative_prompt": "避免的元素",
  "style": "cinematic",
  "resolution": "1080P",
  "aspect_ratio": "9:16",
  "seed": 12345
}
```

### 阶段6: 视频生成

**生成方法**:
- 图生视频（Image-to-Video）
- 运动幅度控制
- 帧率、分辨率设置
- 风格一致性配置

**参数配置**:
```json
{
  "model": "image-to-video-model",
  "duration": 5,
  "frame_rate": 24,
  "motion_strength": "medium",
  "style_consistency": "high"
}
```

### 阶段7: 合成导出

**合成流程**:
1. 视频片段拼接
2. 转场效果添加
3. 音频合成（TTS配音+背景音乐）
4. 字幕生成
5. 最终渲染导出

**输出配置**:
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

## 📥 用户输入

**必需**:
- 创意描述（一句话或完整剧本）

**可选**:
- 风格参考图片
- 角色参考图片
- 目标画幅比例
- 目标时长
- 视觉风格关键词

---

## 📤 最终产出

| 产出项 | 格式 | 说明 |
|--------|------|------|
| 角色设定文档 | JSON + Markdown | 外貌、服装、气质关键词、生图提示词 |
| 场景设定文档 | JSON + Markdown | 空间描述、光线、色调、氛围词 |
| 分镜提示词表 | CSV + JSON | 按幕/场景/镜头三级结构组织 |
| 一致性检查报告 | Markdown | 角色/场景偏差标注 + 修复建议 |
| 完整视频 | MP4 | 合成后的最终视频 |

---

## 🎨 风格控制

### 视觉风格

- **电影感** (cinematic): 专业电影质感
- **动画风** (anime): 二次元动画风格
- **写实风** (realistic): 高度写实的画面
- **艺术风** (artistic): 艺术绘画风格

### 情绪氛围

- 积极/消极
- 温暖/冷淡
- 紧张/放松
- 快乐/悲伤

---

## 🔧 一致性控制策略

### 角色一致性

1. **Seed锁定**: 使用固定种子生成
2. **IP-Adapter**: 参考图像适配
3. **特征锚点**: 关键外貌特征固定
4. **服装追踪**: 跨场次服装管理

### 场景一致性

1. **风格锚点**: 场景风格统一
2. **色彩基调**: 主色调固定
3. **光线设计**: 光源参数一致
4. **空间结构**: 场景布局固定

---

## 📚 专业术语库

### 景别术语

| 景别 | 英文 | 特点 |
|------|------|------|
| 大特写 | Extreme Close-Up | 极近距离，强调细节 |
| 特写 | Close-Up | 面部或物体特写 |
| 中近景 | Medium Close-Up | 胸部以上 |
| 中景 | Medium Shot | 腰部以上 |
| 中远景 | Medium Long Shot | 膝盖以上 |
| 远景 | Long Shot | 全身或场景 |
| 大远景 | Extreme Long Shot | 大范围场景 |

### 运镜术语

| 运镜 | 英文 | 效果 |
|------|------|------|
| 固定 | Static | 静止画面 |
| 推镜头 | Dolly In | 视觉靠近 |
| 拉镜头 | Dolly Out | 视觉远离 |
| 摇镜头 | Pan | 水平转动 |
| 移镜头 | Truck | 水平移动 |
| 跟镜头 | Follow | 跟随主体 |

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/Z5Research/ai-drama-automation.git
cd ai-drama-automation
pip install -r requirements.txt
```

### 配置

```bash
cp config/config.example.json config/config.json
# 编辑config.json，填入你的API密钥
```

### 使用

```python
from ai_drama import DramaPipeline

pipeline = DramaPipeline(config_path="config/config.json")

result = pipeline.generate(
    idea="一个年轻人在咖啡馆遇到多年未见的朋友",
    style="cinematic",
    duration=60
)

print(f"视频已生成: {result.video_path}")
```

---

## 📄 许可证

MIT License

Copyright (c) 2026

---

**为AI内容创作者用心构建**