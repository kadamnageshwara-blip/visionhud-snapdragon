# VisionHUD Engine: Real-Time On-Device Spatial AI & HUD Simulator

VisionHUD Engine is an edge-computed spatial awareness and rider safety platform built for Snapdragon-powered HP laptops. It processes multi-modal vision and audio feeds to output minimalist, low-latency HUD overlays and automated emergency triggers.

## Key Features
- **Qualcomm AI Hub Integration**: Quantized object detection models optimized for Snapdragon NPU via DirectML.
- **Minimalist HUD Interface**: Small, white vector graphics designed to minimize cognitive distraction.
- **Automated Emergency System**: On-device anomaly detection and emergency event dispatch without cloud dependence.
- **Low Power & Thermals**: Leverages Hexagon NPU execution provider for sub-15ms latency and low battery drain.

## Architecture
1. **Input Stream**: Webcam or pre-recorded 1080p dashcam feed.
2. **Inference Pipeline**: ONNX Runtime (DirectML) -> Qualcomm AI Hub Quantized Model.
3. **HUD Engine**: Minimalist white vector renderer over video stream.
4. **Safety Automation**: Collision risk threshold monitor and local emergency call/alert trigger.

## Setup & Execution

### Prerequisites
- Windows 11 on Snapdragon (ARM64)
- Python 3.10+

### Installation
```bash
git clone [https://github.com/kadamnageshwara-blip/visionhud-snapdragon.git](https://github.com/kadamnageshwara-blip/visionhud-snapdragon.git)
cd visionhud-snapdragon
pip install -r requirements.txt
