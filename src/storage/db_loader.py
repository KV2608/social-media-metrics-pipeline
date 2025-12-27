import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.utils.logger import get_logger

load_dotenv()
logger = get_logger()

def load_to_postgres():
    logger.info("Loading data into PostgreSQL")

    engine = create_engine(
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )

    df = pd.read_csv("/tmp/clean_tweets.csv")
    df.to_sql("twitter_metrics", engine, if_exists="append", index=False)

    logger.info("Data successfully loaded")
