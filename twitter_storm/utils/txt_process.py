import re


def tweet_breaker(text, max_size=140):
    tweets = [] 
    if (len(text) > max_size):
        max_size -= 5

    words = re.sub('\s+',' ', text).split(" ")
    
    #first processing
    index = 0
    tweet = []
    while index < len(words):
        if len( (' '.join(tweet) + ' ' +  words[index]).strip() ) <= max_size:
            tweet.append(words[index])
            index += 1
        else:
            tweets.append(tweet)
            tweet = []
    tweets.append(tweet)
    return tweets

def format_tweets(tweets_list, mask):
    size = len(tweets_list)
    i = 0

    while i < size:
        tweets_list[i] = tweets_list[i][0].replace(mask,str(size)) + " ".join(tweets_list[i][1:len(tweets_list[i])])
        i += 1

def add_tweet_index(tweets_list):
    if len(tweets_list) == 1:
        tweets_list[0] = ' '.join(tweets_list[0])
        return
    total = len(tweets_list)
    total_mask = "#"*len(str(total))
    #Check if it fills right
    index = 1

    while index <= total:
        if len( "({}/{})".format(index, total_mask) + " ".join(tweets_list[index-1])   ) <= 140:
            tweets_list[index-1].insert(0,"({}/{})".format(index, total_mask))
        else:
            #Pass the exceeded words forward
            removed = []
            while not(len( "({}/{})".format(index, total_mask) + " ".join(tweets_list[index-1])   ) <= 140):
                removed.insert(0, tweets_list[index - 1].pop())
            
            tweets_list[index-1].insert(0,"({}/{})".format(index, total_mask))
            if index == total:
                tweets_list.append(removed)
                total += 1
            else:
                while len(removed) > 0:
                    tweets_list[index].insert(0, removed.pop())


            
        index += 1

    format_tweets(tweets_list, total_mask)
