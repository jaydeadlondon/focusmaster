# 👁 Focus Master

> AI supervisor. Helps you stay focused and maintain good posture.

This is my personal OpenCV project, which I created to prevent my back from giving out and to boost my productivity while working at the computer.

## 🤔 Why do I even need this?

I noticed that after a couple of hours of work, I either slide under the desk (hello, scoliosis) or, without realizing it, find myself on my phone scrolling through TikTok. **Focus Master** is a “second set of eyes” that watches me through my webcam and keeps me from slacking off.

## ✨ Features

- **Posture Check** — If my shoulders drop too low (I start slouching), an alarm flashes on the screen.
- **Phone Jail** — As soon as a smartphone appears in the frame, the neural network detects it and displays a warning.

## 🛠️ Stack

- **[uv](https://github.com/astral-sh/uv)** — package manager
- **[OpenCV](https://opencv.org/)** — foundation for video capture
- **[Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics)** — neural network
- **[MediaPipe Tasks](https://ai.google.dev/edge/mediapipe/solutions/guide)** — biometrics

## 🚀 How to get started

I use **uv**, so installation takes about 10 seconds:

```bash
uv sync
uv run main.py
```

I wrote this for myself, but if anyone else needs it too — feel free to use it! 🚀
