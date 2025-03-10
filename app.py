from flask import Flask, request, jsonify
from textblob import TextBlob
# from transformers import pipeline  # Uncomment if using transformers


from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['get'])
def hello_func():
    return "hi your flask api is working"


@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text')
    
    # Using TextBlob
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    sentiment_label = 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral'

    # Using Hugging Face transformers
    # classifier = pipeline('sentiment-analysis')
    # result = classifier(text)
    # sentiment_label = result[0]['label']

    return jsonify({'sentiment': sentiment_label})

