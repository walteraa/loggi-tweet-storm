import get_tokens, twitter, os

class TwitterWrapper:

    def __init__(self, auth):
        self.auth = auth

    def auth(self):
        try:
            consumer_key = os.environ['TWITTER_CONSUMER_KEY']
            consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
            auth = get_access_token(consumer_key, consumer_secret)
    except KeyError:
        raise Exception("TWITTER_CONSUMER_KEY or TWITTER_CONSUMER_SECRET missing")
