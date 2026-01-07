#!/bin/sh
set -e

ES_URL="http://elasticsearch:9200"
INDEX_NAME="products_index"

echo "⏳ Waiting for Elasticsearch..."
until curl -s "$ES_URL" >/dev/null; do
  sleep 2
done

echo "✅ Elasticsearch is up"

# 🔥 ENG TO‘G‘RI TEKSHIRUV
if curl -s -o /dev/null -w "%{http_code}" -I "$ES_URL/$INDEX_NAME" | grep -q "200"; then
  echo "ℹ️ Index '$INDEX_NAME' already exists"
  exit 0
fi

echo "🚀 Creating index '$INDEX_NAME'..."

curl -X PUT "$ES_URL/$INDEX_NAME" \
  -H "Content-Type: application/json" \
  -d '{
    "settings": {
      "analysis": {
        "analyzer": {
          "default": { "type": "standard" }
        }
      }
    },
    "mappings": {
      "properties": {
        "id": { "type": "long" },
        "title": { "type": "text" },
        "description": { "type": "text" },
        "category": { "type": "keyword" },
        "price": { "type": "float" },
        "is_active": { "type": "boolean" },
        "created_at": { "type": "date" }
      }
    }
  }'

echo "🎉 Index '$INDEX_NAME' created successfully"
