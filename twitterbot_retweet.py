import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter bot which retweets,like tweets and follow users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

        try:
            client.retweet(tweet.id)
            print("Retweeted the tweet")

            if LIKE:
                client.like(tweet.id)
                print("Liked the tweet")

            if FOLLOW and not tweet.user.following:
                client.follow(tweet.user.id)
                print("Followed the user")

        except Exception as error:
            print(error)

        sleep(SLEEP_TIME)

stream = MyStream(bearer_token = bearer_token)

rule = tweepy.StreamRule(f"({QUERY})(-is:retweet -is:reply)" )
stream.add_rules(rule)
stream.filter()
