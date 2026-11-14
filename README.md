# 🧠 Image Classification App

A deep learning image classification application built using **PyTorch** and **Streamlit**. The application uses a custom Convolutional Neural Network (CNN) to classify uploaded images into one of three categories: **Cat, Dog, or Person**.

## 🚀 Features

- Upload images in JPG, JPEG, and PNG formats.
- Classify images into Cat, Dog, or Person categories.
- Custom CNN architecture built using PyTorch.
- Display the uploaded image and its predicted class.
- Generate and display an image with the predicted label.
- Simple and interactive Streamlit interface.

## 🛠️ Technologies Used

- **Python** – Programming language
- **PyTorch** – Deep learning framework
- **Torchvision** – Image preprocessing and transformations
- **OpenCV** – Image processing and annotation
- **Pillow (PIL)** – Image loading and manipulation
- **Streamlit** – Web application framework

## 📁 Project Structure

```text
image-classifier/
│
├── app.py                  # Streamlit application
├── requirements.txt        # Project dependencies
│
├── core/
│   ├── __init__.py
│   └── predict.py          # CNN model and prediction logic
│
└── model/
    ├── __init__.py
    └── cnn_model.pth       # Trained CNN model weights
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aniket-bapat/image-classifier.git
```

### 2. Navigate to the project directory

```bash
cd image-classifier
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧠 Model Information

The project uses a custom Convolutional Neural Network (CNN) implemented in PyTorch.

The model consists of:
- Convolutional layers
- Batch Normalization
- ReLU activation functions
- Max Pooling layers
- Fully connected layers

### Supported Classes

| Class Index | Prediction |
|---|---|
| 0 | Cat |
| 1 | Dog |
| 2 | Person |

Input images are resized to **128 × 128 pixels** and normalized before being passed to the model.

🌐 Live Demo

Try the deployed application here:

🚀: [Open Image Classification App](https://imageclassification-njtqzwge6yxuspxuo5a7qy.streamlit.app/)

## 📌 Future Improvements

- Improve model accuracy and generalization.
- Add confidence scores for predictions.
- Support additional image categories.
- Improve the user interface.
- Add model performance visualizations.

## 👨‍💻 Author

**YOUR NAME**

GitHub: [Aniket-Bapat](https://github.com/Aniket-bapat)

---

⭐ If you find this project interesting, consider giving the repository a star!