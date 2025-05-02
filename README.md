# Gesture Detection Using YOLOv8

This project implements real-time hand gesture detection using a custom-trained YOLOv8 model. The system allows users to capture labeled gesture images, train a detection model using Ultralytics YOLOv8, and perform real-time gesture recognition via webcam.

## 📁 Project Structure

<pre>

.
└── Gesture-Detection-Using_Yolov8/
    ├── Capture Images/
    │   ├── main.py # Script to capture labeled images from webcam
    │   └── captured_images/ # Folder created from script to store labeled image datasets
    ├── Notebook/
    │   └── DIP_LAB_PROJECT_FINAL.ipynb
    ├── Weights/
    │   └── best.pt # Custom-trained YOLOv8 model weights
    ├── GROUP_MEMBERS.txt
    ├── Gesture Detection ~ PROJECT REPORT.pdf
    ├── gesture_detection.py # Real-time gesture detection using YOLOv8
    └── README.md # Project documentation

</pre>
## 🧠 Project Workflow

### 1. Image Collection

Use the `capture_images.py` script to collect labeled hand gesture images via webcam:

```bash

python capture_images.py

````

By default, this script:

* Opens the webcam.
* Captures 500 images labeled with a specific gesture name (e.g., "Yes", "No", etc.).
* Stores them in the `captured_images/` folder under a subfolder with the label name.

You can adjust the label and number of images in the script:

```python
	label_name = "Yes"
	output_directory = "captured_images"
```

### 2. Model Training

Training is performed using the provided Jupyter Notebook:

📓 `Notebook/DIP_LAB_PROJECT_FINAL.ipynb`

The notebook covers:

* Data preprocessing and annotation format for YOLOv8.
* Custom training with Ultralytics YOLOv8.
* Exporting trained weights to `Weights/best.pt`.

**Note:** Visit the original training notebook here for reference and edits:
[GitHub Link](https://github.com/AbdulMoizZuberi/Gesture-Detection-Using_Yolov8/blob/master/Notebook/DIP_LAB_PROJECT_FINAL.ipynb)

### 3. Real-Time Gesture Detection

Run the real-time detection script:

```bash
	python gesture_detection.py
```

This will:

* Load the webcam stream.
* Use the trained YOLOv8 model (`Weights/best.pt`) to detect gestures.
* Display the detected gesture bounding boxes and labels on-screen.

Press **'q'** to quit.



## 🔧 Requirements

Ensure the following versions are installed:

| PACKAGE       	| VERSION        	|
|---------------	|----------------	|
| Python        	| 3.13           	|
| numpy         	| 2.2.1          	|
| opencv-python 	| 4.10.0.84      	|
| ultralytics   	| Latest YOLO v8 	|

Install dependencies with:

```bash
	pip install numpy==2.2.1 opencv-python==4.10.0.84 ultralytics
```



## ✅ Features

* Easy dataset creation via webcam.
* YOLOv8-based gesture detection.
* Real-time gesture classification with bounding boxes.
* Modular structure for training and deployment.


## 📌 Future Work

* Add support for more gestures and classes.
* Improve dataset diversity (backgrounds, lighting).
* Integrate gesture-based controls (e.g., media control, navigation).


## Authors

* Abdul Moiz Zuberi
  GitHub: [AbdulMoizZuberi](https://github.com/AbdulMoizZuberi)

## 📜 License

This project is open-source and available under the MIT License.
