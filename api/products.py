from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.session import get_db
from models import Product, Category
from schemas.product import ProductCreate, ProductResponse
from services.product_analytics import log_product_view
from services.product_indexer import index_product

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse)
async def create_product(
    data: ProductCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    product = Product(**data.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)

    category_name = None
    if product.category_id:
        res = await db.execute(
            select(Category.name).where(Category.id == product.category_id)
        )
        category_name = res.scalar_one_or_none()
    data = {
            "id": product.id,
            "title": product.title,
            "description": product.description,
            "price": float(product.price),
            "is_active": product.is_active,
            "category": category_name
        }
    background_tasks.add_task(
        index_product,
        data,
    )

    return product



@router.get("/", response_model=list[ProductResponse])
async def list_products(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(Product).where(Product.is_active == True))
    return res.scalars().all()


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    request: Request,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Product).where(Product.id == product_id, Product.is_active == True)
    )
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # 🔥 CLICKHOUSE VIEW EVENT
    background_tasks.add_task(
        log_product_view,
        product.id,
        request.client.host
    )

    return product
