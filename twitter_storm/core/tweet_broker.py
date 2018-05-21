"""Core module used to orchestrate the queue consumption and the tweet sending"""
import twitter
from twitter_storm.utils.get_tokens import get_access_token
from twitter_storm.utils.txt_process import tweet_breaker, add_tweet_index
from twitter_storm.utils.tweet_queue import TweetQueue

class TweetBroker(object):
    """A broker class which manages all processing and send tweets process"""
    def __init__(self, consumer_key, consumer_secret, text):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.text = text
        self.auth = None
        self.twitter_api = None
        self.tweet_id = None
        self.queue = None

    def do_auth(self):
        """Initiate an authorization process"""
        self.auth = get_access_token(self.consumer_key, self.consumer_secret)

    def prepare(self):
        """Prepare the tweets queue and the Twitter API to be used to send tweets"""
        if self.auth is None:
            raise Exception("You should authenticate and authorize twitter API before prepare")

        tweets = tweet_breaker(self.text)
        add_tweet_index(tweets)
        self.queue = TweetQueue(tweets)
        self.twitter_api = twitter.Api(consumer_key=self.auth['consumer_key'], consumer_secret=self.auth['consumer_secret'], access_token_key=self.auth['token_key'], access_token_secret=self.auth['token_secret'])

    def start(self):
        """Starts the process of send processed tweets by consuming a queue"""
        if self.queue is None or self.twitter_api is None:
            raise Exception("You should prepare the tweets before start")

        while not self.queue.is_empty():
            tweet = self.queue.pop()
            if self.tweet_id is None:
                status = self.twitter_api.PostUpdate(tweet)
                self.tweet_id = status.id
            else:
		self.twitter_api.PostUpdate(tweet, in_reply_to_status_id=self.tweet_id)
        print "Your twitter was posted in https://twitter.com/{}/status/{}".format(self.twitter_api.VerifyCredentials().screen_name, self.tweet_id)
