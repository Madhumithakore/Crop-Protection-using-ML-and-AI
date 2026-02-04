from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = load_model('final_pest_classifier_model.h5')

# Manually define class labels
class_labels = ['ants', 'bees', 'beetle', 'caterpillar', 'earthworms', 'earwig', 
                'grasshopper', 'moth', 'slug', 'snail', 'wasp', 'weevil']

# Medicine mapping dictionary
medicine_mapping = {
    "ants": "Use Organic Neem Spray",
    "bees": "No treatment necessary — beneficial",
    "beetle": "Apply Sevin Dust or Neem Oil",
    "caterpillar": "Use Bacillus Thuringiensis (BT) Spray",
    "earthworms": "No treatment — beneficial for soil",
    "earwig": "Use oil traps",
    "grasshopper": "Apply Neem Oil or Nolo Bait",
    "moth": "Set up Pheromone Traps",
    "slug": "Use Iron Phosphate bait",
    "snail": "Install Copper Tape Barriers",
    "wasp": "Apply Wasp Spray carefully",
    "weevil": "Use Pyrethrin Sprays or Neem extract"
}

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded."

    file = request.files['file']
    if file.filename == '':
        return "No selected file."

    # Save uploaded file
    filepath = os.path.join('static', file.filename)
    file.save(filepath)

    # Preprocess the image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    pred = model.predict(img_array)
    confidence = np.max(pred)
    predicted_class_index = np.argmax(pred)
    predicted_class = class_labels[predicted_class_index]

    # Smart decision
    if confidence >= 0.80:
        treatment = medicine_mapping.get(predicted_class, "No treatment info available.")
        result = f"Pest Detected: {predicted_class} (Confidence: {confidence*100:.2f}%)\nTreatment: {treatment}"
    else:
        result = "Model not confident enough to classify reliably. Please try another image."

    return render_template('result.html', result=result, image_path=filepath)


if __name__ == '__main__':
    app.run(debug=True)

#cd pest-detection-ultimate
#python app.py