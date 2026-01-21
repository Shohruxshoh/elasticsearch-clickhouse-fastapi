# 🚀 ElasticSearch + ClickHouse Analytics Service

This project is a **production-ready analytics backend** built with **FastAPI**, **Elasticsearch**, and **ClickHouse**. It is designed to collect, index, and analyze **product and search behavior data** with high performance and scalability in mind.

The system is suitable for **real-time analytics**, **search statistics**, and **high-load analytical workloads**.

---

## ✨ Features

* 🔍 **Elasticsearch**

  * Full-text search
  * Fast filtering and aggregations
  * Product indexing

* 📊 **ClickHouse**

  * High-performance analytical database
  * Time-series analytics
  * Aggregated statistics

* ⚡ **FastAPI**

  * High-speed async REST API
  * Auto-generated Swagger documentation

* 📈 Analytics APIs

  * Product statistics
  * Search statistics
  * Time-series analytics

---

## 🧱 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Elasticsearch**
* **ClickHouse**
* **Uvicorn**
* **Pydantic**
* **Docker & Docker Compose**

---

## 📂 Project Structure

```
elastic_and_clickhouse/
│
├── main.py              
├── .env                    
│
├── api/                   
│   ├── products.py
│   ├── categories.py\│   ├── search.py
│   └── analytics.py
│
├── core/                  
│   └── config.py
│
├── services/              
│   ├── elastic.py
│   ├── clickhouse.py
│   ├── product_indexer.py
│   ├── product_analytics.py
│   ├── product_stats.py
│   ├── search_analytics.py
│   ├── search_stats.py
│   └── search_timeseries.py
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
APP_NAME=Elastic ClickHouse Analytics
DEBUG=true

ELASTIC_HOST=http://elasticsearch:9200
ELASTIC_INDEX=products_index

CLICKHOUSE_HOST=clickhouse
CLICKHOUSE_PORT=8123
CLICKHOUSE_DB=default
```

---

## 🐳 Running with Docker (Recommended)
---

### 3️⃣ Start the project

```bash
docker-compose up --build -d
```

---

## 🌐 API Documentation

Once the services are running:

* Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔁 Application Startup Flow

* Waits for ClickHouse to be available
* Connects to Elasticsearch
* (Optional) Creates Elasticsearch index if not exists
* Starts FastAPI application

---

## 📊 Analytics Flow

### Search Analytics

1. User sends search request
2. Elasticsearch performs the search
3. Search event is saved to ClickHouse
4. Analytics endpoints provide:

   * Search count
   * Popular queries
   * Time-series statistics

### Product Analytics

1. Product is created or updated
2. Product data is indexed into Elasticsearch
3. User interactions are stored in ClickHouse
4. Statistics are calculated via analytics APIs

---

## 🎯 Use Cases

* E-commerce analytics
* Search behavior tracking
* High-load analytical systems
* Real-time dashboards
* Microservice-based architectures

---

## 🚀 Future Improvements

* Kafka for event ingestion
* Background processing (Celery / Async workers)
* Grafana dashboards (ClickHouse)
* Authentication & rate limiting
* Kubernetes deployment

---

## 🧑‍💻 Author

Built for scalable, real-world analytics systems using modern backend technologies.
