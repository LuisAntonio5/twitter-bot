import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

CONSUMER_KEY_TWITTER = os.getenv("CONSUMER_KEY_TWITTER")
CONSUMER_SECRET_TWITTER = os.getenv("CONSUMER_SECRET_TWITTER")
ACCESS_TOKEN_TWITTER = os.getenv("ACCESS_TOKEN_TWITTER")
ACCESS_TOKEN_SECRET_TWITTER = os.getenv("ACCESS_TOKEN_SECRET_TWITTER")

auth = tweepy.OAuthHandler(CONSUMER_KEY_TWITTER, CONSUMER_SECRET_TWITTER)
auth.set_access_token(ACCESS_TOKEN_TWITTER, ACCESS_TOKEN_SECRET_TWITTER)

api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

api.update_status("this tweet was made through a bot")
# api.create_friendship("luisantoniolds")

