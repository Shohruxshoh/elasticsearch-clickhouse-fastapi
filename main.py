from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from api.products import router as products_router
from api.categories import router as categories_router
from api.search import router as search_router
from api.analytics import router as analytics_router
from services.clickhouse import wait_for_clickhouse
from services.elastic import create_index_if_not_exists


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # ===============================
    # CORS
    # ===============================
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # prod’da aniq domen beriladi
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ===============================
    # ROUTERS
    # ===============================
    app.include_router(categories_router)
    app.include_router(products_router)
    app.include_router(search_router)
    app.include_router(analytics_router)

    # ===============================
    # HEALTH CHECK
    # ===============================
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {
            "status": "ok",
            "app": settings.app_name
        }

    @app.on_event("startup")
    async def startup_event():
        wait_for_clickhouse()
        # create_index_if_not_exists()

    return app


app = create_app()
