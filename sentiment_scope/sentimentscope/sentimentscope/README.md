 SentimentScope – Django Sentiment Analysis App
📌 Overview

SentimentScope is a Django-based web application that performs sentiment analysis on user-entered text using TextBlob.
It classifies text as Positive, Negative, or Neutral and displays polarity, subjectivity, and confidence scores.

🚀 Features

Sentiment classification (Positive / Neutral / Negative)

Polarity & subjectivity score display

Confidence level estimation

Input validation

Clean Django MVC architecture

Responsive UI with Bootstrap

🛠 Tech Stack

Backend: Django

NLP: TextBlob

Frontend: HTML, CSS, Bootstrap

Language: Python

⚙️ Setup
pip install -r requirements.txt
python -m textblob.download_corpora
python manage.py migrate
cd sentimentscope
python manage.py runserver


Open: http://127.0.0.1:8000/

🔍 Sentiment Logic

Polarity > 0.1 → Positive

Polarity < -0.1 → Negative

Else → Neutral

