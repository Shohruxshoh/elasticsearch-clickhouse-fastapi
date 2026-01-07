from services.clickhouse import ch_client


def get_top_viewed_products(limit: int = 10):
    query = f"""
        SELECT
            product_id,
            count() AS views
        FROM product_view_events
        GROUP BY product_id
        ORDER BY views DESC
        LIMIT {limit}
    """

    result = ch_client.query(query)

    return [
        {
            "product_id": row[0],
            "views": row[1]
        }
        for row in result.result_rows
    ]
