import time
from elasticsearch import Elasticsearch
from core.config import settings

es_client = Elasticsearch(
    settings.elastic_host,
    verify_certs=False,
    request_timeout=30
)

INDEX_NAME = settings.elastic_index


def create_index_if_not_exists():

    if es_client.indices.exists(index=INDEX_NAME):
        return

    body = {
        "settings": {
            "analysis": {
                "analyzer": {
                    "default": {
                        "type": "standard"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "id": {"type": "long"},
                "title": {"type": "text"},
                "description": {"type": "text"},
                "category": {"type": "keyword"},
                "price": {"type": "float"},
                "is_active": {"type": "boolean"},
                "created_at": {"type": "date"}
            }
        }
    }

    es_client.indices.create(
        index=INDEX_NAME,
        body=body
    )
