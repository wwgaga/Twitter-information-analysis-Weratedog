import tweepy
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAAszogEAAAAAAMJ4KXu40ZLEPLIHKR%2FXYdQGBl0%3D1RwvMLS7IYFqb0w7fI9RoaDP7wrdhFAUaWm3zX43Y9vNb2baFM')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)