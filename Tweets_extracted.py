# -*- coding: utf-8 -*-
"""Tweepy Api: IndvsAus tweets extraction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/112EyuQ1cehzRNJJqtiXAH9o6tK52j8ku
"""


# The original code was witten in google collaboratory.It is preferred over jupyter notebook for deep learning and NLP applications.
# Mounting notebook to google dive to export our csv file containing tweets directly. 
from google.colab import drive
drive.mount('/content/drive')

#Installing necessary libraries 
!pip install tweepy
import os
import tweepy as tw

# To access the Twitter API, you will need 4 things from the your Twitter App page. These keys are located in your Twitter app settings in the Keys and Access Tokens tab. 
#You need to get yourself approved before extracting tweets(https://developer.twitter.com/en/products/twitter-api/early-access)
apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
apisecretkey = 'xxxxxxxxxxxxxxxxxxxxxx'
accesstoken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
accesstokensecret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


#calling OAuthHandler required for authentication with Twitter

auth = tw.OAuthHandler(apikey,apisecretkey) 
auth.set_access_token(accesstoken,accesstokensecret)

# Initialize tweepy API with rate limit notification set i.e simply notifying on reaching the limit to extract number of tweets.
api = tw.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Input your search phrase. The API allows for searching for last 7 days(freee version). 
# Applying date ranges operators which simply outputs twitter data between specific dates. If not applied the API will return most recent tweets.
# You can apply whole host of different search operators and parameters Found here(https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators)
search_word = '#IndvsAus' or '#AusvsInd'
date_since = '2021-01-20'
date_until = '2021-01-21'


# Cursor object handles all the pagination work for us.
# Passing parameters into the API method.Eg: filtering retweets, english language, Tweet_mode gives the full text of the tweet
# Count is set at 1000. The free version can only process about 3200 tweets in a day.
tweets = tw.Cursor(api.search,q = search_word+' -filter:retweets', lang ='en',tweet_mode='extended',since = date_since,until= date_until).items(1000)


# Header row for our spreadsheet. 
tweet_details = [[tweet.id_str,tweet.full_text,tweet.created_at,tweet.user.location]for tweet in tweets]
tweet_details

# Creating a pandas dataframe that containd the data
import pandas as pd
tweetdf = pd.DataFrame(data=tweet_details,columns=['tweet_id','Full_text','tweet_timestamp','user_location'])
pd.set_option('max_colwidth',800)
tweetdf.head(10)

# Exporting our csv file to local directory/google drive.
tweetdf.to_csv(r'C:\Users\91987\Desktop\Twitter Sentiment Analysis\File Name.csv', index = False)

