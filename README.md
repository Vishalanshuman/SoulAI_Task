PDF Document Classifier API
Introduction
This is a simple project that creates an API to read and classify PDF documents. The goal is to determine if the PDF document is about categories like warranty, transactions, troubleshooting, etc. The API takes a PDF file, extracts the text, and classifies it using a pre-trained machine learning model.

Requirements
Before you can run this project, make sure you have the following:

Python 3.7+ installed on your computer.
Pip (Python package manager) to install the required libraries.
Installation Steps
Here’s how to get the project running:

Clone the Project:

First, download or clone the project from the repository:

bash
Copy code
git clone <repository-url>
cd pdf_classifier
Set Up Virtual Environment (Optional):

It’s a good idea to use a virtual environment to keep your Python packages isolated. Run these commands:

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install Dependencies:

After setting up the virtual environment (or if you skip it), install the required packages by running:

bash
Copy code
pip install -r requirements.txt
This will install all the necessary Python packages like Flask, PyPDF2, scikit-learn, and joblib.

Train the Model (Optional):

You don’t need to do this step unless you want to train the model again from scratch. If so, run:

bash
Copy code
python train_model.py
This will create the machine learning model and save it as text_classifier_model.pkl and tfidf_vectorizer.pkl.

Run the API:

Now that everything is set up, you can start the API with:

bash
Copy code
python app.py
This will start the server at http://127.0.0.1:5000.

How to Use the API
Endpoint: /classify
This is the main endpoint where you upload your PDF file to classify it.

Method: POST
URL: http://127.0.0.1:5000/classify
Data: A pdf file is required. You can use a tool like Postman or curl to send the file.
Example Request Using Curl
Here’s an example using the curl command to send a PDF file:

bash
Copy code
curl -X POST -F "pdf=@path_to_your_pdf_file.pdf" http://127.0.0.1:5000/classify
Response
The API will return the category of the document in JSON format. For example:

json
Copy code
{
    "category": "warranty"
}
Project Structure
Here’s a quick overview of the project structure:



Flask: To create the API.
PyPDF2: To extract text from PDF files.
scikit-learn: For building the machine learning model.
joblib: To save and load the machine learning model.
Common Issues
Packages Not Installing: Make sure you are using a virtual environment to avoid conflicts with other Python projects. If you still face issues, try installing the packages individually.
Invalid PDF Files: Make sure the PDF you upload is a valid file. If the text cannot be extracted, it might be due to the PDF format.
Model Prediction Not Accurate: The model is simple and may need better training data for more accurate results. You can improve it by adding more documents for training.
Future Improvements
Here are some ideas for improving the project:

Add more categories for classifying documents.
Improve the machine learning model with more advanced techniques like BERT.
Add error handling for corrupted or unreadable PDF files.