import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the necessary dataset for sentiment analysis
sid = SentimentIntensityAnalyzer()

# text = 'I really enjoyed the movie. It was fantastic'
# sentiment_score = sid.polarity_scores(text)

text1 = 'I hate you ! I dont wanna see you again !'
sentiment_score = sid.polarity_scores(text1)

positive_score = sentiment_score['pos']
negative_score = sentiment_score['neg']

if positive_score > negative_score:
    print("The text has a positive sentiment.")
elif positive_score < negative_score:
    print("The text has a negative sentiment.")
else:
    print("The text is neutral.")
