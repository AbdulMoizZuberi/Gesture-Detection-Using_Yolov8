import cv2
from ultralytics import YOLO

model = YOLO('Weights/best.pt')

def detect_gestures():
    # Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return
    print("Press 'q' to quit the real-time detection.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not read properly. Exiting...")
            break

        results = model(frame)

        annotated_frame = results[0].plot()  # Automatically annotates detections

        cv2.imshow("Gesture Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_gestures()