from textblob import TextBlob

text = "The movie was amazing and I really enjoyed it."

blob = TextBlob(text)

print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

if blob.sentiment.polarity > 0:
    print("Positive Sentiment")
elif blob.sentiment.polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")