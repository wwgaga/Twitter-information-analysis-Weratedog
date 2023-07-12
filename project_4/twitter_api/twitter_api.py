import tweepy
#import configparser
import pandas as pd
import json
'''
# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
'''
# read twitter archive
df = pd.read_csv('twitter-archive-enhanced.csv')
#print(df['tweet_id'][:3])

api_key  = 'Mxg6aCZavmUSBxFvKu6UEkctx'
api_secret = 'hEgHdqwJpStPyoVWDxIlx7nEgAIYPrcazY1XxhxHRMiCEWFFp8'

access_token = '835972361665019904-zf8eLHBmDWKB6hZUWIwr19LbGYFz4d0'
access_token_secret = 'eyywWWiYc8Ph4LqRoc5mRrtOPBIgv2Jc5XIcPhFMyTBfB'

# authenticate
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# create api object
api = tweepy.API(auth,wait_on_rate_limit=True)

print(api.verify_credentials())

'''
for tweet_id in df['tweet_id'][:3]:
    tweet = api.get_status(tweet_id, tweet_mode='extended')
    print(tweet.full_text)

failed_tweet = []
with open('tweet_json.txt', mode='w', encoding='utf-8') as file:
    for tweet_id in df['tweet_id']:
        try:
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            tweet_json = json.dumps(tweet._json)
            # write tweet JSON data line by line
            file.write(tweet_json + '\n')
        except:
            failed_tweet.append(tweet_id)

df_list = []
with open('tweet_json.txt', mode='r', encoding='utf-8') as file:
    lines = file.readlines()
    # read tweet JSON data line by line
    for line in lines:
        data = json.loads(line)
        tweet_id = data['id']
        retweet_count = data['retweet_count']
        favorite_count = data['favorite_count']
        df_list.append({'tweet_id': tweet_id, 'retweet_count': retweet_count, 'favorite_count': favorite_count})
tweet_data = pd.DataFrame(df_list, columns=['tweet_id', 'retweet_count', 'favorite_count'])
print(failed_tweet)
'''