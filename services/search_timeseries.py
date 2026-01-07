from services.clickhouse import ch_client


def get_search_timeseries(
    interval: str = "minute",
    limit: int = 60
):
    if interval == "minute":
        time_func = "toStartOfMinute(event_time)"
        alias = "minute"
    elif interval == "hour":
        time_func = "toStartOfHour(event_time)"
        alias = "hour"
    elif interval == "day":
        time_func = "toStartOfDay(event_time)"
        alias = "day"
    else:
        raise ValueError("Invalid interval")

    query = f"""
        SELECT
            {time_func} AS {alias},
            count() AS total
        FROM search_events
        GROUP BY {alias}
        ORDER BY {alias} DESC
        LIMIT {limit}
    """

    result = ch_client.query(query)

    return [
        {
            "time": row[0],
            "count": row[1]
        }
        for row in result.result_rows
    ]
