# -*- coding: utf-8 -*-
"""Skin_Disease_detection_project_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1whnHNBOFr0tXviiKOoZZTB5PLonQIPQn
"""

import zipfile
import os

# Define the path to the ZIP file and the extraction directory
zip_file_path = '/content/skin disease.zip'
extract_dir = '/content/skin disease'

# Create the extraction directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

# Extract the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# 2. Preprocess Image Function
def preprocess_image(image_path, target_size=(255, 255)):
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to create a batch
    return img_array

# 3. Load Pre-Trained Model
model = load_model('skin disease model (4).h5')
x = preprocess_image(r"/content/skin disease/skin disease/Validation/Melanoma/ISIC_7304751.jpg")

# 5. Make Predictions
predictions = model.predict(x)

# 6. Define Class Labels Dictionary
class_labels = {
    0: 'Atopic Dermatitis',
    1: 'Eczema',
    2: 'Melanoma'
    # Add more class indices and labels as needed
}

# 7. Get Predicted Class Index and Label
predicted_class_index = np.argmax(predictions[0])
predicted_class_label = class_labels[predicted_class_index]

# 8. Print Predicted Disease
print("Predicted Disease:", predicted_class_label)

