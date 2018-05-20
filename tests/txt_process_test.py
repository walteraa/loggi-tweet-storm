from twitter_storm.utils.txt_process import *
import unittest

class TestTweetBreak(unittest.TestCase):

    tweets_list = tweet_breaker("Lorem ipsum dolor sit amet, duo at regione inimicus mediocrem. Duo rebum copiosae ut, regione sadipscing qui at, primis iuvaret torquatos at nam. Esse aliquam invidunt pri an. Et ridens docendi nec. Cu labitur indoctum appellantur mei. Usu summo consequat et. Erat labore in sea.Ius ad mutat primis, ad qui solum labores. Nec at nonumy ullamcorper. Vero errem vel ut. Ad nam aliquip molestiae, an debitis scriptorem has. At sea dictas vivendo, te usu laudem salutandi.Ea vix purto iuvaret. Vim ad nominavi urbanitas, ne cum etiam malorum menandri. Tantas tritani equidem per in. Ex quo altera meliore. Cu melius persius fabellas vis, sea erat propriae gubergren ea. Legendos instructior est at, te mei cibo aeque, vix malis ponderum abhorreant te. Cu ferri semper animal vel. Reque incorrupte omittantur pro cu. Nihil quaeque delicatissimi id per, ne dictas propriae oporteat mel. Qui deleniti reformidans at, vim numquam aliquam constituto ea, vim ex interesset definitiones. Pri ex probatus eleifend, sea prima tempor ei. Tota offendit gloriatur duo te, eu quo summo eripuit honestatis, quo mutat graece convenire ei. Urbanitas prodesset cu mei, propriae maiestatis qui no. Nullam gloriatur sea cu. Ne sea summo expetendis.", 140)

    def test_length(self):
        self.assertEquals( len(self.tweets_list), 10)

    def test_tweet_index(self):
        add_tweet_index(self.tweets_list)
        assert "(1/10)" in self.tweets_list[0] 
        assert "(10/10)" in self.tweets_list[len(self.tweets_list) - 1]

    def test_size_of_tweet(self):
        for tweet in self.tweets_list:
            assert len(tweet) <= 140

    def test_tweets_type(self):
        for tweet in self.tweets_list:
            self.assertEquals(type(tweet), type(""))
        

    def test_uniquetweet_breaker(self):
        original_text = "Lorem ipsum dolor sit amet, duo at regione inimicus mediocrem."
        unique_tweet =  tweet_breaker(original_text, 140)
        self.assertEquals(len(unique_tweet), 1)
        add_tweet_index(unique_tweet)
        assert "(1/1)" not in unique_tweet[0]
        self.assertEquals(type(unique_tweet[0]), type(""))

