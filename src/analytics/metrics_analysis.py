import pandas as pd
from src.utils.logger import get_logger

logger = get_logger()

def analyze_metrics():
    logger.info("Analyzing engagement metrics")

    df = pd.read_csv("/tmp/clean_tweets.csv")
    df["engagement_score"] = df["likes"] + df["retweets"]

    kpis = {
        "total_tweets": len(df),
        "average_likes": df["likes"].mean(),
        "average_retweets": df["retweets"].mean(),
        "average_engagement": df["engagement_score"].mean()
    }

    pd.DataFrame([kpis]).to_csv("/tmp/kpis.csv", index=False)
    logger.info("KPI metrics generated")
