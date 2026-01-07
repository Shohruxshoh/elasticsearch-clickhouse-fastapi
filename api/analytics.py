from fastapi import APIRouter, Query
from services.product_stats import get_top_viewed_products
from services.search_stats import get_top_search_queries
from services.search_timeseries import get_search_timeseries

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/top-searches")
async def top_searches(
        limit: int = Query(10, ge=1, le=100)
):
    items = get_top_search_queries(limit)
    return {
        "items": items
    }


@router.get("/top-viewed-products")
async def top_viewed_products(
        limit: int = Query(10, ge=1, le=100)
):
    items = get_top_viewed_products(limit)
    return {
        "items": items
    }


@router.get("/search-timeseries")
async def search_timeseries(
        interval: str = Query("minute", pattern="^(minute|hour|day)$"),
        limit: int = Query(60, ge=1, le=500)
):
    items = get_search_timeseries(interval=interval, limit=limit)
    return {
        "interval": interval,
        "items": items
    }
