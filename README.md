# Sign Language Recognition

This project is a **Sign Language Recognition System** that uses deep learning to classify sign language gestures. The application features a backend built with Flask and TensorFlow, and a frontend built using HTML, CSS, and JavaScript, providing a seamless and user-friendly interface. The project enables real-time recognition of sign language gestures, helping bridge communication gaps for individuals who use sign language.

---

## Features
- **Real-Time Sign Language Recognition**: Upload an image of a sign language gesture to predict its corresponding letter or digit.
- **Responsive Frontend**: Built with Bootstrap and custom CSS, the interface is modern and user-friendly.
- **Deep Learning Backend**: A convolutional neural network (CNN) model trained on a dataset of sign language gestures.
- **Cross-Origin Integration**: The app integrates a secure CORS-enabled Flask backend with the frontend.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
    - [Clone the Repository](#clone-the-repository)
    - [Backend Setup](#backend-setup)
    - [Frontend Setup](#frontend-setup)
4. [How to Run](#how-to-run)
5. [Screenshots](#screenshots)
6. [License](#license)

---

## Project Overview
This application aims to provide an accessible tool for recognizing sign language gestures using machine learning. It consists of:
- **Backend**: A Flask API that processes uploaded images, performs preprocessing, and predicts the gesture using a pre-trained deep learning model.
- **Frontend**: A responsive webpage allowing users to upload images, view predictions, and see a preview of their uploaded image.

---

## Technologies Used

- **Frontend**:
  - HTML, CSS, JavaScript
  - Bootstrap (CSS Framework)

- **Backend**:
  - Python (Flask Framework)
  - TensorFlow and Keras (Deep Learning Library)
  - Flask-CORS (Cross-Origin Resource Sharing)

- **Additional Tools**:
  - OpenCV (Image Processing)
  - NumPy

---

## Setup Instructions

### Clone the Repository
To start using this project, clone the repository:
```bash
git clone https://github.com/your-username/sign-language-recognition.git
cd sign-language-recognition
```

### Backend Setup
Navigate to the `backend` folder:
```bash
cd backend
```

#### Install Dependencies
Ensure you have Python 3.7 or later installed. Install the required dependencies:
```bash
pip install -r requirements.txt
```


## **Model Weights**
The pretrained model weights are **not included** in the repository due to size limitations. To use this project:
1. Retrain the weights from the notebook provided.

2. Place the downloaded `model_weights.weights.h5` file in the `backend/model_weights/` directory.


#### Run the Backend
Start the Flask server:
```bash
python3 app.py
```
The backend will run on `http://127.0.0.1:5000` by default.

### Frontend Setup
Navigate to the `frontend` folder:
```bash
cd ../frontend
```

Open the `index.html` file in a browser:
```bash
open index.html
```
Alternatively, you can host the frontend using a simple HTTP server:
```bash
python3 -m http.server
```
Access the frontend at `http://127.0.0.1:8000`.

---

## How to Run
1. Start the Flask backend:
   ```bash
   python3 backend/app.py
   ```
2. Open the `frontend/index.html` file in a browser.
3. Upload an image of a sign language gesture.
4. View the predicted letter or digit displayed on the webpage.

---

## Screenshots

### Main Interface
![Main Interface](static/screenshots/main-interface.png)

### Prediction Results
![Prediction Results](static/screenshots/prediction-results.png)

---

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to use and modify this project for educational and personal purposes.

---

## Contributing
Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request with your changes.

---

## Contact
If you have any questions or issues, please contact:
- **Name**: Muhammad Sheraz
- **Email**: sheraz.ds.pucit@gmail.com
- **GitHub**: [Muhammad-Sheraz-ds](https://github.com/Muhammad-Sheraz-ds)
- **Linked In**: [Muhammad Sheraz](https://www.linkedin.com/in/muhammad-sheraz-5b3887242/)

