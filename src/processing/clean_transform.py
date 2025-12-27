import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()

def clean_data():
    logger.info("Cleaning and transforming data")

    df = pd.read_csv("/tmp/raw_tweets.csv")
    df.drop_duplicates(inplace=True)
    df["created_at"] = pd.to_datetime(df["created_at"])

    df.to_csv("/tmp/clean_tweets.csv", index=False)
    logger.info("Clean data saved")
