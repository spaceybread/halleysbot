import datetime
from dateutil.relativedelta import *
import tweepy
import time

consumer_key ="***"
consumer_secret ="***"
access_token ="***"
access_token_secret ="***"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

hopeImAlive = datetime.date(2061, 7, 27)


today = datetime.date.today()

wait = hopeImAlive - today

delta = relativedelta(hopeImAlive, today)

phrase = "Halley's Commet next perihelion is in " + str(delta.years) + ' years, ' + str(delta.months) + ' months, and ' + str(delta.days) + ' days' #or simply ' + str(wait)

api.update_status(status = phrase)
print(phrase)
phrase = ""
today = ""
