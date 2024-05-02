import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from deep_translator import GoogleTranslator
from textblob import TextBlob

def get_tweets_by_username(username, limit=20):
    url = "https://twitter154.p.rapidapi.com/user/tweets"
    querystring = {
        "username": username,
        "limit": str(limit),
        "include_replies": "false",
        "include_pinned": "false"
    }
    headers = {
        "X-RapidAPI-Key": "05fa33d2f8msh576bc036c3679edp1f00fejsnf02955142329",
        "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print("Failed to retrieve tweets. Status code:", response.status_code)
        return []

def get_tweets_by_hashtag(hashtag, limit=20):
    url = "https://twitter154.p.rapidapi.com/hashtag/hashtag"
    querystring = {
        "hashtag": hashtag,
        "limit": str(limit),
        "section": "top"
    }
    headers = {
        "X-RapidAPI-Key": "05fa33d2f8msh576bc036c3679edp1f00fejsnf02955142329",
        "X-RapidAPI-Host": "twitter154.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print("Failed to retrieve tweets by hashtag. Status code:", response.status_code)
        return []

def translate_text(text, source_lang="auto", target_lang="en"):
    translated = GoogleTranslator().translate(text, source=source_lang, target=target_lang)
    return translated

def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

st.title('Emotional Intelligence')

# User choice: Hashtag or Username
option = st.sidebar.selectbox('Choose analysis type', ('Hashtag', 'Username'))

# Fetch tweets based on user input
if option == 'Hashtag':
    hashtag = st.sidebar.text_input('Enter hashtag')
    tweets = get_tweets_by_hashtag(hashtag)
else:
    username = st.sidebar.text_input('Enter username')
    tweets = get_tweets_by_username(username)

# Data preprocessing and analysis
if tweets:
    df = pd.DataFrame(tweets)
    df['translated_text'] = df['text'].apply(translate_text)
    df['sentiment'] = df['translated_text'].apply(analyze_sentiment)

    # Display sentiment distribution
    st.subheader('Sentiment Distribution')
    fig = px.histogram(df, x='sentiment', title='Sentiment Distribution')
    st.plotly_chart(fig)

    # Display sentiment pie chart
    st.subheader('Sentiment Pie Chart')
    fig = px.pie(df, names='sentiment', title='Sentiment Pie Chart')
    st.plotly_chart(fig)

    # Display list of fetched tweets
    st.subheader('List of Fetched Tweets')
    st.write(df)

    # Display sentiment over time (line chart)
    st.subheader('Sentiment Over Time')
    df['creation_date'] = pd.to_datetime(df['creation_date'])
    daily_sentiments = df.groupby([df['creation_date'].dt.date, 'sentiment']).size().unstack(fill_value=0).reset_index()
    melted_df = daily_sentiments.melt(id_vars='creation_date', var_name='sentiment', value_name='count')
    fig = px.line(melted_df, x='creation_date', y='count', color='sentiment', title='Sentiment Over Time')
    st.plotly_chart(fig)

    # Count the number of tweets for each sentiment category and plot emotions distribution
    emotion_count = df['sentiment'].value_counts().reset_index()
    emotion_count.columns = ['Emotion', 'Count']
    emotion_mapping = {
        'Positive': 'joy',
        'Negative': 'sadness',
        'Neutral': 'neutral'
    }
    emotion_count['Emotion'] = emotion_count['Emotion'].map(emotion_mapping)
    missing_emotions = set(['joy', 'sadness', 'fear', 'anger', 'surprise', 'neutral']) - set(emotion_count['Emotion'])
    missing_df = pd.DataFrame({'Emotion': list(missing_emotions), 'Count': [0] * len(missing_emotions)})
    emotion_count = pd.concat([emotion_count, missing_df])
    emotion_count = emotion_count.sort_values(by='Emotion', ascending=True)
    fig = px.bar(emotion_count, x='Emotion', y='Count', title='Emotions Distribution')
    st.plotly_chart(fig)

else:
    st.write('No tweets found.')
