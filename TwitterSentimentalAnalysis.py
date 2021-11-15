from textblob import TextBlob
import tweepy
import sys

mykeys = open('secret.txt', 'r').read().splitlines()

apikey = mykeys[0]
apikey_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key = apikey, consumer_secret= apikey_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = input("Input a keyword to get it's polarity: ")
tweet_amount = 200
polarity = 0

positive = 0
negative = 0
neutral = 0

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

for tweet in tweets:
    final_tweet = tweet.text.replace('RT', '')
    if final_tweet.startswith(' @'):
        position = final_tweet.index(':')
        final_tweet = final_tweet[position+2:]
    if final_tweet.startswith('@'):
        position = final_tweet.index(' ')
        final_tweet = final_tweet[position+2:]
    analysis = TextBlob(final_tweet)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0.000000:
        positive += 1
    elif tweet_polarity < 0.000000:
        negative += 1
    elif tweet_polarity == 0.000000:
        neutral += 1

    polarity += tweet_polarity


print("polarity of "+search_term+" is: ", polarity)
print(f'\nAmount of positive tweets: {positive}')
print(f'Amount of negative tweets: {negative}')
print(f'Amount of neutral tweets: {neutral}')
