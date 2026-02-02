from django.shortcuts import render

from django.shortcuts import render
from textblob import TextBlob

def sentiment_analyzer(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        sentiment = "Positive 😊"
        confidence = "High" if polarity > 0.5 else "Medium"
    elif polarity < -0.1:
        sentiment = "Negative 😠"
        confidence = "High" if polarity < -0.5 else "Medium"
    else:
        sentiment = "Neutral 😐"
        confidence = "Low"

    return sentiment, round(polarity, 3), round(subjectivity, 3), confidence

def home(request):
    result = None

    if request.method == "POST":
        text = request.POST.get("text")

        if not text or len(text.strip()) < 5:
            result = {"error": "Please enter at least 5 characters."}
        else:
            sentiment, polarity, subjectivity, confidence = sentiment_analyzer(text)
            result = {
                "sentiment": sentiment,
                "polarity": polarity,
                "subjectivity": subjectivity,
                "confidence": confidence
            }

    return render(request, "analyzer/index.html", {"result": result})

# Create your views here.
