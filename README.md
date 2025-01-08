# CurrencyDetection

This project uses the YOLOv8 model to detect various Indian currency denominations in real-time through a webcam feed. The program loads a trained YOLO model (best.pt) and annotates the video frames with detected currency denominations, including their confidence levels.

## Features
- **YOLOv8**: Utilizes the latest YOLO capabilities for robust and accurate detection.
- **Real-Time Detection**: Detects objects in real-time using a webcam.
- **Currency Recognition**: Identifies various denominations of Indian currency, including both coins and notes.
- **Confidence Scoring**: Displays confidence levels for each detection alongside bounding boxes.
## Project Structure
- **currency_detection.py**: Main Python script for object detection and webcam integration.
- **Model File (best.pt)**: Pre-trained YOLO model for currency detection.
- **Class Names**: A list of supported currency denominations used for annotation.
## Requirements
### Software:
- Python 3.8 or later
- YOLOv8 by Ultralytics
- OpenCV for Python
### Hardware:
- A computer with a functional webcam.
- GPU acceleration (optional, but recommended for better performance).

## Future Work

- Implement real-time voice-guided feedback for detected objects.
- Expand the model to recognize currencies from other regions.
## Class Labels
The program recognizes the following currency denominations:

- **Coins**: 1 rupee coin, 2 rupee coin, 5 rupee coin, 10 rupee coin, 20 rupee coin
- **Notes**: 1 rupee, 2 rupees, 5 rupees, 10 rupees, 20 rupees, 50 rupees, 100 rupees, 200 rupees, 500 rupees, 2000 rupees
