import tweepy
# Authenticate with OAuth 2.0 Bearer Token (App only)
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAAszogEAAAAAUrVVkyFBGFexnJ6V5IiTN4sZ7Pc%3DxJawavtxaSaVnlxHZ0Yn4LtZG7UKgqbRA0vxfE5QKpU72yISLz')

# Pull tweets from twitter
query = '#elonmusk -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
# Get tweets that contain the hashtag #TypeKeywordHere
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
# print pulled tweets
for tweet in tweets.data:
    print('\n**Tweet Text**\n',tweet.text)