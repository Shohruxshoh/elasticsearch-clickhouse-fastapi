from fastapi import APIRouter, Query, BackgroundTasks, Request
from services.elastic import es_client, INDEX_NAME, create_index_if_not_exists
from services.search_analytics import log_search_event

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/")
async def search_products(
    request: Request,
    background_tasks: BackgroundTasks,
    q: str = Query(..., min_length=2),
    limit: int = 10,
    offset: int = 0
):
    query_body = {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": q,
                        "fields": ["title^3", "description"],
                        "fuzziness": "AUTO"
                    }
                }
            ],
            "filter": [
                {"term": {"is_active": True}}
            ]
        }
    }

    response = es_client.search(
        index=INDEX_NAME,
        query=query_body,
        from_=offset,
        size=limit
    )

    total = response["hits"]["total"]["value"]

    # 🔥 CLICKHOUSE EVENT (BACKGROUND)
    background_tasks.add_task(
        log_search_event,
        q,
        total,
        request.client.host
    )

    hits = [
        {
            "id": hit["_source"]["id"],
            "title": hit["_source"]["title"],
            "price": hit["_source"]["price"],
            "score": hit["_score"]
        }
        for hit in response["hits"]["hits"]
    ]

    return {
        "query": q,
        "total": response["hits"]["total"]["value"],
        "items": hits
    }
