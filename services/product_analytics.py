from datetime import datetime
from services.clickhouse import ch_client
from core.config import settings

def log_product_view(
    product_id: int,
    user_ip: str
):
    ch_client.insert(
        table=f"{settings.clickhouse_db}.product_view_events",
        data=[
            [
                datetime.utcnow(),
                product_id,
                user_ip
            ]
        ],
        column_names=[
            "event_time",
            "product_id",
            "user_ip"
        ]
    )
