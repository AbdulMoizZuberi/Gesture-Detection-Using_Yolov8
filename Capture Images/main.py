import cv2
import os


def capture_images(label: str, output_folder: str, num_images: int = 500):
    """
    Capture images from webcam and save them in labeled folders.

    Args:
        label (str): Label name for the images (e.g., "Person_A").
        output_folder (str): Path to the output folder where images will be stored.
        num_images (int): Number of images to capture (default is 500).
    """
    # Create the output directory if it doesn't exist
    label_folder = os.path.join(output_folder, label)
    os.makedirs(label_folder, exist_ok=True)

    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return

    print(f"Starting image capture for label '{label}'.")
    print("Press 'q' to quit early.")

    # Capture images
    count = 0
    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read from the webcam.")
            break

        # Display the frame
        cv2.imshow("Webcam", frame)

        # Save the frame to the labeled folder
        image_path = os.path.join(label_folder, f"{label}_{count:03d}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Captured image {count + 1}/{num_images}: {image_path}")

        count += 1

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting early due to user input.")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    print(f"Image capture completed. Images saved to: {label_folder}")


# Example usage
if __name__ == "__main__":
    # Change these paths/labels as needed
    label_name = "Yes"
    output_directory = "captured_images"
    capture_images(label_name, output_directory)