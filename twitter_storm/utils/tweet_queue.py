"""Module to add Queue data structures and its variations used to app data management"""
class TweetQueue(object):
    """Queue data structure to manage tweets"""
    def __init__(self, list_of_tweets):
        self.tweets = list_of_tweets

    def pop(self):
        """Remove and return the top element"""
        value = self.tweets[0]
        del self.tweets[0]
        return value

    def is_empty(self):
        """Return True if the queue is empty"""
        return len(self.tweets) == 0
