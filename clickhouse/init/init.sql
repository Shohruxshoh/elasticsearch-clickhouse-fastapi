CREATE DATABASE IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.search_events (
    event_time     DateTime,
    query          String,
    results_count  UInt32,
    user_ip        String
)
ENGINE = MergeTree
ORDER BY event_time;

CREATE TABLE IF NOT EXISTS analytics.product_view_events (
    event_time   DateTime,
    product_id   UInt64,
    user_ip      String
)
ENGINE = MergeTree
ORDER BY (product_id, event_time);
