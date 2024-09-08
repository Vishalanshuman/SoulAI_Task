from flask import Flask, request, jsonify
import PyPDF2
import os
import joblib

app = Flask(__name__)

# Load pre-trained classification model and vectorizer
model = joblib.load('text_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def classify_text(text):
    vectorized_text = vectorizer.transform([text])
    prediction = model.predict(vectorized_text)[0]
    return prediction

@app.route('/classify', methods=['POST'])
def classify_pdf():
    if 'pdf' not in request.files:
        return jsonify({"error": "No PDF file provided"}), 400
    
    pdf = request.files['pdf']
    file_path = os.path.join("/tmp", pdf.filename)
    pdf.save(file_path)

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)

    # Classify the extracted text
    category = classify_text(text)

    # Clean up - remove the temporary PDF file
    os.remove(file_path)

    return jsonify({"category": category})

if __name__ == '__main__':
    app.run(debug=True)
