CREATE TABLE IF NOT EXISTS twitter_metrics (
    tweet_id BIGINT PRIMARY KEY,
    text TEXT,
    likes INTEGER,
    retweets INTEGER,
    created_at TIMESTAMP
);
