import os
from flask import Flask, render_template, request
from transformers import pipeline

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

sentiment_analyzer = pipeline("sentiment-analysis")

from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the pre-trained sentiment analysis pipeline
# This automatically downloads a model from Hugging Face
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_text = request.form.get('text')
        if user_text:
            # Get prediction
            prediction = sentiment_analyzer(user_text)[0]
            result = f"Sentiment: {prediction['label']} (Confidence: {round(prediction['score'], 2)})"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)