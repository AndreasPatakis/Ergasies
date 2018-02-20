import tweepy
import collections
from tweepy import OAuthHandler

consumer_key = 'RIei9UXWx800R3X8ioPcW7HSA'
consumer_secret = 'L7qL94GrSxIPQnEpD3Tj07iSpCkppDGBUOjacM77QOKHxkMLRl'
access_token = '246712918-hxqIC7PdvKN74Gtid4MYENrF2Qm1njrBzM21aMwx'
access_secret = 'YkSMPZi5F5XswZdLay8jwvRKRpMP3BSsFmKLgPIhlEi0o'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

last_tweets=''
f=True

while f:
    name = raw_input("Give a twitter account name: ")
    if (name[0] != '@'):
        name = '@' + name
    try:
        timeline = api.user_timeline(screen_name=name, include_rts=True, count=10)
        break
    except tweepy.TweepError:

        print 'User does not exist.Please try again.'



for tweet in timeline:
        last_tweets = last_tweets + ' ' + tweet.text

last_tweets=last_tweets.split(' ')

arithmos_leksis=[]
for i in range(len(last_tweets)):
    arithmos_leksis.append(0)
    for leksi in last_tweets:
        if leksi==last_tweets[i]:
            arithmos_leksis[i]+=1
max_word=max(arithmos_leksis)


#xwris tin vivliothiki collections

#p=0
#while f:
#    if (max_word==arithmos_leksis[p]):
#        print 'The most used word out of the first 10 tweets of',name,' is "',last_tweets[p],'" and it was used',max_word,'times.'
#        f=False
#    p+=1

#me tin vivliothiki collections

counter = collections.Counter(last_tweets)
first=counter.most_common()

print 'The most used word out of the first 10 tweets of',name,' is "',first[0][0],'" and it was used',first[0][1],'times.'
