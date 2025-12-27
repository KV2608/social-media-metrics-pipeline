import tweepy
import pandas as pd
import os
from dotenv import load_dotenv
from src.utils.logger import get_logger

load_dotenv()
logger = get_logger()

def fetch_tweets():
    logger.info("Fetching Twitter data")

    client = tweepy.Client(
        bearer_token=os.getenv("TWITTER_BEARER_TOKEN")
    )

    query = "data analytics OR machine learning"
    response = client.search_recent_tweets(
        query=query,
        max_results=100,
        tweet_fields=["created_at", "public_metrics"]
    )

    records = []
    if response.data:
        for tweet in response.data:
            records.append({
                "tweet_id": tweet.id,
                "text": tweet.text,
                "likes": tweet.public_metrics["like_count"],
                "retweets": tweet.public_metrics["retweet_count"],
                "created_at": tweet.created_at
            })

    df = pd.DataFrame(records)
    df.to_csv("/tmp/raw_tweets.csv", index=False)
    logger.info("Twitter data saved")
