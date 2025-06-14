# 🎛️ Volume Control Using Hand Gestures

A computer vision project that allows users to control their system volume using simple hand gestures — completely touch-free. This is achieved using a webcam, MediaPipe for hand tracking, OpenCV for visualization, and Pycaw to control the system audio.

## 📸 How It Works

- The webcam captures real-time video.
- MediaPipe detects and tracks hand landmarks.
- The distance between the **thumb tip** and **index finger tip** is calculated.
- This distance is mapped to a volume range using the `pycaw` audio library.
- Visual feedback (volume bar, percentage, and FPS) is displayed using OpenCV.

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
