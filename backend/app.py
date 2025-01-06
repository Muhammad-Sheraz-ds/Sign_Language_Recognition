import os
import cv2
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from flask_cors import CORS
# Disable GPU (if CUDA issues persist)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Initialize Flask app
app = Flask(__name__)
CORS(app) 
# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define image size and channels
image_size = 64
img_channel = 3

# Define the model
model = Sequential()
# Block 1
model.add(Conv2D(32, 3, activation='relu', padding='same', input_shape=(image_size, image_size, img_channel)))
model.add(Conv2D(32, 3, activation='relu', padding='same'))
model.add(MaxPooling2D(padding='same'))
model.add(Dropout(0.2))
# Block 2
model.add(Conv2D(64, 3, activation='relu', padding='same'))
model.add(Conv2D(64, 3, activation='relu', padding='same'))
model.add(MaxPooling2D(padding='same'))
model.add(Dropout(0.3))
# Block 3
model.add(Conv2D(128, 3, activation='relu', padding='same'))
model.add(Conv2D(128, 3, activation='relu', padding='same'))
model.add(MaxPooling2D(padding='same'))
model.add(Dropout(0.4))
# Fully connected layers
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))
# Output layer
model.add(Dense(36, activation='softmax'))

# Load pre-trained weights
weights_path = os.path.join(os.path.dirname(__file__), 'model_weights/model_weights.h5')
try:
    model.load_weights(weights_path)
    print(f"Model weights loaded successfully from {weights_path}")
except FileNotFoundError:
    print(f"Error: Model weights file not found at {weights_path}. Please ensure the file exists.")
except Exception as e:
    print(f"Error loading weights: {e}")

# Define categories (0-9 and a-z)
categories = {i: chr(97 + i) if i >= 10 else str(i) for i in range(36)}

# Preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (image_size, image_size))
    image = image / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)
    return image

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save uploaded file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        # Preprocess and predict
        image = preprocess_image(file_path)
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        label = categories[predicted_class]
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up uploaded file
        os.remove(file_path)

    return jsonify({"prediction": label})

if __name__ == '__main__':
    app.run(debug=True)
