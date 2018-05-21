from core.tweet_broker import TweetBroker
import sys, os

def main():
    if len(sys.argv) != 2:
        print("You should run main by running the following command:\n\npython main.py \"The text you would like to send\"" )
        exit(1)
    no_variables = False
    if not os.environ.has_key('TWITTER_CONSUMER_KEY'):
        print("You should define TWITTER_CONSUMER_KEY environment variable")
        no_variables = True
    if not os.environ.has_key('TWITTER_CONSUMER_SECRET'):
        print("You should define TWITTER_CONSUMER_SECRET environment variable")
        no_variables = True

    if no_variables:
        exit(1)

    tweet_broker = TweetBroker(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'], sys.argv[1])
    tweet_broker.do_auth()

    tweet_broker.prepare()

    tweet_broker.start()
if __name__ == "__main__":
    main()
