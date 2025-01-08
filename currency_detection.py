import cv2
from ultralytics import YOLO

# Load the trained YOLO model
model = YOLO('best.pt')  # Update this path if needed

# Open the webcam (0 is the default camera; change if you have multiple webcams)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Set video frame dimensions (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Class names from your dataset
class_names = [
    "1 rupee", "1 rupee coin", "10 rupee coin", "10 rupees", "100 rupees",
    "2 rupee", "2 rupee coin", "20 rupee coin", "20 rupees", "200 rupees",
    "2000 rupees", "5 rupee", "5 rupee coin", "50 rupees", "500 rupees"
]

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame from webcam.")
        break

    # Run YOLO object detection
    results = model(frame)

    # Annotate the frame with detection results
    for result in results[0].boxes:
        # Extract bounding box, confidence, and class
        x1, y1, x2, y2 = map(int, result.xyxy[0])
        confidence = result.conf.item()
        print(confidence)
        class_id = int(result.cls[0].item())

        # Get the class name
        class_name = class_names[class_id]

        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display class name and confidence
        label = f"{class_name} {confidence:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow("YOLO Object Detection", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
