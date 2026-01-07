from datetime import datetime

from core.config import settings
from services.clickhouse import ch_client


def log_search_event(
    query: str,
    results_count: int,
    user_ip: str
):
    ch_client.insert(
        table=f"{settings.clickhouse_db}.search_events",
        data=[
            [
                datetime.utcnow(),
                query,
                results_count,
                user_ip
            ]
        ],
        column_names=[
            "event_time",
            "query",
            "results_count",
            "user_ip"
        ]
    )
