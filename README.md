# ✋ Hand Tracking & Volume Control

## 📋 Summary
In this project, I built a gesture-based volume controller using hand landmark detection. The system tracks the distance between the thumb and index finger in real time and maps it directly to the system audio volume — no keyboard, no mouse, just your hand.

## Features

- Real-time hand landmark detection (21 keypoints)
- Finger distance mapped to volume level (0–100%)
- Visual feedback: volume bar and percentage on screen
- Smooth, responsive gesture control

## Tech Stack

| Tool | Role |
|------|------|
| Python | Core language |
| MediaPipe | Hand landmark detection |
| OpenCV | Video capture and rendering |
| Pycaw | Windows audio control |
| NumPy | Distance interpolation |

## How It Works

1. MediaPipe detects 21 hand landmarks per frame
2. The distance between thumb tip and index finger tip is calculated
3. That distance is interpolated to a 0–100% volume range
4. `pycaw` sets the system volume in real time



> **Note:** Audio control via `pycaw` is Windows-only. The hand tracking module works cross-platform.

## Project Structure
