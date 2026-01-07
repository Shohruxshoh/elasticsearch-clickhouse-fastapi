import time

import clickhouse_connect
from core.config import settings

ch_client = clickhouse_connect.get_client(
    host=settings.clickhouse_host,
    port=settings.clickhouse_port,
    username=settings.clickhouse_user,
    password=settings.clickhouse_password,
    database=settings.clickhouse_db
)


def wait_for_clickhouse(max_retries: int = 60, delay: int = 2):
    for i in range(max_retries):
        try:
            client = ch_client
            client.command("SELECT 1")
            print("✅ ClickHouse is READY")
            return
        except Exception:
            print(f"⏳ Waiting for ClickHouse... ({i + 1})")
            time.sleep(delay)

    raise RuntimeError("❌ ClickHouse is not ready")
