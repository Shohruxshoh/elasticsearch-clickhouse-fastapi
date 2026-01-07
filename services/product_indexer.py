from services.elastic import es_client, INDEX_NAME
from models import Product


def index_product(product: dict):
    doc = {
        "id": product.get("id"),
        "title": product.get("title"),
        "description": product.get("description"),
        "category": product.get("category"),
        "price": float(product.get("price")),
        "is_active": product.get("is_active"),
        "created_at": product.get("created_at"),
    }

    es_client.index(
        index=INDEX_NAME,
        id=product.get("id"),
        document=doc
    )
