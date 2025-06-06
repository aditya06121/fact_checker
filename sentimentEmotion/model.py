from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

from preContent.dataPrep import dataPrep

# Load models and tokenizers
sentiment_model_name = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)

emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)

# Label mappings
sentiment_labels = ['Negative', 'Neutral', 'Positive']
emotion_labels = ['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']

def predict_sentiment(text):
    inputs = sentiment_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = sentiment_model(**inputs)
    scores = F.softmax(outputs.logits, dim=1)[0]
    max_score_idx = torch.argmax(scores).item()
    return {"label": sentiment_labels[max_score_idx], "score": scores[max_score_idx].item()}

def predict_emotion(text):
    inputs = emotion_tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = emotion_model(**inputs)
    scores = F.softmax(outputs.logits, dim=1)[0]
    max_score_idx = torch.argmax(scores).item()
    return {"label": emotion_labels[max_score_idx], "score": scores[max_score_idx].item()}


if __name__=="__main__":
    raw_text=dataPrep("https://www.deccanherald.com/india/karnataka/bengaluru/chinnaswamy-stampede-four-including-rcb-marketing-manager-arrested-3573945")

    sentiment_result = predict_sentiment(raw_text)
    emotion_result = predict_emotion(raw_text)

    print("Sentiment Analysis Result:", sentiment_result)
    print("Emotion Analysis Result:", emotion_result)