# HappyLens 😊
A real-time computer vision project for smile detection using facial landmarks.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Dlib](https://img.shields.io/badge/Dlib-Facial%20Landmarks-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

HappyLens is a **real-time smile detection system** built using **Python, OpenCV, and dlib**.
The application captures video from a webcam, detects faces, and analyzes facial landmarks to determine whether a person is smiling.

By leveraging the **68-point facial landmark model**, HappyLens identifies key facial features such as the mouth, eyes, and jawline and uses them to analyze facial expressions in real time.

This project demonstrates practical applications of **computer vision**, **facial analysis**, and **real-time video processing**.

---

## Demo

Example of the system detecting a smile in real time.

![Smile Detection Demo](assets/demo.gif)

---

## Screenshot

Example frame from the smile detection system.

![Project Screenshot](assets/screenshot.png)

---

## Features

* Real-time face detection using OpenCV
* Facial landmark detection using dlib's **68-point landmark model**
* Smile detection through mouth landmark analysis
* Live webcam video processing
* FPS monitoring for performance tracking
* Modular and scalable project structure

---

## Technologies Used

* **Python**
* **OpenCV**
* **dlib**
* **NumPy**

---

## Project Structure

```
smile_detection_system/
│
├── main.py                     # Main application entry point
├── config.py                   # Configuration settings
├── requirements.txt            # Project dependencies
│
├── detectors/
│   ├── face_detector.py        # Face detection logic
│   └── smile_detector.py       # Smile detection logic
│
├── utils/
│   ├── landmarks.py            # Facial landmark utilities
│   └── fps.py                  # FPS calculation utility
│
└── models/
    └── shape_predictor_68_face_landmarks.dat   # Pretrained facial landmark model
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ma5Codes/happylens.git
```

### 2. Navigate to the project folder

```bash
cd happylens
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the application with:

```bash
python main.py
```

The system will open your webcam and start detecting faces and smiles in real time.

---

## How It Works

1. The webcam captures live video frames.
2. A **face detector** identifies faces in the frame.
3. The **dlib 68-point facial landmark model** extracts facial feature points.
4. The system analyzes **mouth landmarks** to determine if the person is smiling.
5. The result is displayed in real time on the video feed.

---

## Future Improvements

Possible enhancements:

* Emotion detection (happy, sad, surprised, etc.)
* Smile intensity measurement
* Face recognition integration
* Web dashboard interface
* Dataset logging for ML training

---

## Author

Built as a **computer vision project exploring facial expression analysis using OpenCV and dlib**.

