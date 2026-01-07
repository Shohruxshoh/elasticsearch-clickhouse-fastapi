from services.clickhouse import ch_client


def get_top_search_queries(limit: int = 10):
    query = f"""
        SELECT
            query,
            count() AS total
        FROM search_events
        GROUP BY query
        ORDER BY total DESC
        LIMIT {limit}
    """

    result = ch_client.query(query)

    return [
        {
            "query": row[0],
            "count": row[1]
        }
        for row in result.result_rows
    ]
