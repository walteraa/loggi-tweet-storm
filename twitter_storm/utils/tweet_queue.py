class TweetQueue:
    
    def __init__(self, list_of_tweets):
        self.tweets = list_of_tweets

    def pop(self):
       value = self.tweets[0]
       del self.tweets[0]
       return value

    def is_empty(self):
       return len(self.tweets) == 0

