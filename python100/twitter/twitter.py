import boto3
import json
import tweepy.streaming
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob



 
k='wLYuZBCLzWTRgoKtjSrxiLnfI'
ks='3swo0bvSs3oOWDzNQ8eVdUk64v2sYiCWXju91rjPYG7beUA6hQ'
At='1584483687374036992-lfjBiDZolOJ09au1NG6Rm1zfH173tZ'
Ts='tuICnCgoItyuoTSMH1gbDCWa2KK2x8mcQIN2ZuLmWXJNq'
auth = OAuthHandler(k,ks)
auth.set_access_token(At,Ts)

stream=tweepy.Stream(k,ks,At,Ts)
stream.sample()






