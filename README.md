# 🎛️ Volume Control Using Hand Gestures

A computer vision project that enables users to control system volume using hand gestures in real time. The system uses a webcam, MediaPipe for hand tracking, OpenCV for video processing, and Pycaw to interface with Windows audio controls. Just move your fingers to turn the volume up or down — no buttons needed!

---

## 📽️ How It Works

This project captures real-time video through a webcam and identifies hand landmarks using MediaPipe. It tracks the distance between the thumb and index finger tips. The closer your fingers are, the lower the volume; the farther apart they are, the louder the system becomes.

- 🟢 **Pinch fingers together** ➡️ Volume down  
- 🔵 **Spread fingers apart** ➡️ Volume up

The system dynamically maps finger distance to the system's volume level using Pycaw, and provides visual feedback using OpenCV (volume bar, FPS, etc.).

---

## 🧠 Code Overview

### 🔹 `HandTrackingModule.py`

Contains the `HandDetector` class for detecting and extracting hand landmark positions using MediaPipe.

#### ✅ Key Components:

- **`__init__`**: Initializes MediaPipe Hands with desired configuration (max hands, confidence, etc.).
- **`findHands(img, draw=True)`**: Converts the BGR image to RGB, processes it through MediaPipe, and draws landmarks on the image.
- **`findPosition(img, handNo=0, draw=True)`**: Returns a list of landmarks with their (x, y) coordinates.

## ✨ Features

- Real-time hand tracking using MediaPipe
- Smooth volume control with natural gestures
- Visual volume bar and percentage overlay
- FPS counter to monitor performance
- Touchless user interface ideal for smart environments and accessibility

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – for capturing and displaying video
- **MediaPipe** – for hand landmark detection
- **Pycaw** – for controlling system volume
- **NumPy** and **Math** – for interpolation and distance calculation

## Project Structure

├── HandTrackingModule.py       # Hand detection class using MediaPipe

├── VolumeHandControl.py        # Main script for volume control

└── README.md                   # Project documentation

## ❗ Notes
This project works only on Windows due to the use of Pycaw.

Add support for Linux/macOS volume control (e.g., using osascript or amixer).

The range [15, 150] for finger distance can be tweaked to better match your hand size and camera distance.

Make sure the webcam has enough lighting for reliable hand detection.



## 🧰 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Maheswara23/volume-control-hand-gesture.git
   cd volume-control-hand-gesture

2. Install   required libraries:
   ```bash
   pip install opencv-python mediapipe pycaw comtypes numpy

3. Run the Project
   ```bash
   python VolumeHandControl.py

