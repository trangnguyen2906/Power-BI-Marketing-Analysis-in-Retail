#!/usr/bin/env python
# coding: utf-8

# # Import Library

# In[85]:


import pandas as pd
import pyodbc # for connecting SQL Server
import nltk # for transforming text
nltk.download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer 


# # Fetch Data from SQL server

# In[86]:


# Define a function to fetch data from SQL Server 
def fetch_data_SQL_server():
    connection_string = (
        "Driver={SQL Server};"
        "Server=localhost\\SQLEXPRESS;"
        "Database=mkt_analysis;"
        "Trusted_Connection=yes;"
    )
    # Create a connection to the SQL Server database
    conn = pyodbc.connect(connection_string)
    # Define the SQL query to fetch data
    query = "SELECT * FROM mkt_analysis.dbo.customer_reviews"
    #Execute the query and fetch the data into a DataFrame
    df = pd.read_sql(query, conn)
    conn.close()  # Close the connection
    return df
df_customer_reviews = fetch_data_SQL_server()
df_customer_reviews['ReviewDate'] = pd.to_datetime(df_customer_reviews['ReviewDate'], errors='coerce')  # Convert ReviewDate to datetime
df_customer_reviews.head()


# # Sentiment Analyzer

# In[87]:


analyzer = SentimentIntensityAnalyzer()
analyzer.lexicon.update({ "top-notch": 3.0, "five": 4.5, "Exceeded": 4.0, "Quick delivery": 3.5})
# Define a function to calculate sentiment score using VADER
def sentiment_calculate(review):
    #get the sentiment score for the reviews
    score = analyzer.polarity_scores(review)
    # Return the compound score
    return score['compound']
sentiment_calculate("Five stars for the quick delivery.")  # Example usage


# In[88]:


# Define a function to categorize sentiment based on both the sentiment score and rating score
def categorize_sentiment(score, rating):
    if score > 0.05:  # Positive sentiment score
        if rating >= 4:
            return 'Positive'  # High rating score and positive sentiment score 
        elif rating == 3:
            return 'Conflicted Positive'  # Neutral rating score but positive sentiment score
        else:
            return 'Conflicted Negative'  # Low rating score but positive sentiment score
    elif score < -0.05:  # Negative sentiment score
        if rating <= 2:
            return 'Negative'  # Low rating score and negative sentiment score
        elif rating == 3:
            return 'Conflicted Negative'  # Neutral rating score but negative sentiment score
        else:
            return 'Conflicted Positive'  # High rating score but negative sentiment score
    else:  # Neutral sentiment score
        if rating >= 4:
            return 'Positive'  # High rating score with neutral sentiment score
        elif rating <= 2:
            return 'Negative'  # Low rating score with neutral sentiment score
        else:
            return 'Neutral'  # Neutral rating score and neutral sentiment score


# In[89]:


# Define a function to define / group sentiment buckets based on the sentiment score
def sentiment_group(score):
    if score >= 0.5:
        return '0.5 to 1.0' # Strongly positive sentiment
    if 0.0 <= score < 0.5:
        return '0.0 to 0.49' # Positive sentiment
    if -0.5 <= score < 0.0:
        return '-0.49 to 0.0'  # Negative sentiment
    if score < -0.5:
        return '-1.0 to -0.5'  # Strongly negative sentiment


# In[ ]:


# Apply sentiment analysis to calculate sentiment scores for each review
df_customer_reviews['SentimentScore'] = df_customer_reviews['ReviewText'].apply(sentiment_calculate)

# Apply sentiment categorization using both text and rating
df_customer_reviews['SentimentCategory'] = df_customer_reviews.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)

# Apply sentiment bucketing to categorize scores into defined ranges
df_customer_reviews['SentimentGroup'] = df_customer_reviews['SentimentScore'].apply(sentiment_group)

# Display the first few rows of the DataFrame with sentiment scores, categories, and buckets
print(df_customer_reviews.head())

# Convert the DataFrame to a CSV file
df_customer_reviews.to_csv('fact_customer_reviews_sentiment.csv', index=False)


# In[ ]:




