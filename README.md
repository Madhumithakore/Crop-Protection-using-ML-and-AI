# 🌿 Revolutionizing Crop Protection Using Machine Learning & AI

This project presents an AI-powered solution for crop protection by detecting agricultural pests from images using deep learning and suggesting appropriate treatment. It leverages a EfficientNetB0 and a web interface built using Flask.

---

## 📸 Use Case

> **Problem:** Manual pest identification is time-consuming and error-prone for farmers.  
> **Solution:** Upload an image of a pest, and the AI model classifies it into one of 12 pest types and suggests the correct treatment.

---

## 🧠 Model Details

- **Architecture**: EfficientNetB0
- **Classes**: ants, bees, beetle, caterpillar, earthworms, earwig, grasshopper, moth, slug, snail, wasp, weevil
- **Framework**: TensorFlow & Keras
- **Accuracy Achieved**: ✅ 86% validation accuracy after fine-tuning
- **Training Data**: ~100 images per class (manually curated)

---

## 🖥️ Technologies Used

| Tool          | Purpose                      |
|---------------|------------------------------|
| `Python`      | Programming Language          |
| `TensorFlow`  | Deep Learning Framework       |
| `Flask`       | Web Framework                 |
| `HTML/CSS`    | Frontend Styling              |
| `Git/GitHub`  | Version Control & Deployment  |

---

## 🚀 How It Works

1. User uploads pest image via web UI
2. Flask backend processes and feeds image to the AI model
3. Model classifies the pest and returns:
   - Pest Name
   - Confidence Score
   - Recommended Treatment
4. UI displays result with pest image

---


