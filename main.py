"""FastAPI application for testing CI/CD and static code analysis."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Test API",
    description="A test API for GitHub Actions CI and static code analysis",
    version="1.0.0",
)


class Item(BaseModel):
    """Item model for testing."""

    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ItemResponse(BaseModel):
    """Response model for item operations."""

    name: str
    total_price: float


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to FastAPI Test API"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/items/", response_model=ItemResponse)
async def create_item(item: Item) -> ItemResponse:
    """
    Create a new item and calculate total price.

    Args:
        item: Item details including name, price, and optional tax

    Returns:
        ItemResponse with calculated total price

    Raises:
        HTTPException: If price is negative
    """
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")

    total_price = item.price + (item.tax if item.tax else 0)
    return ItemResponse(name=item.name, total_price=total_price)


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int | str]:
    """
    Read an item by ID.

    Args:
        item_id: The ID of the item to retrieve

    Returns:
        Dictionary containing item ID and a message
    """
    return {"item_id": item_id, "message": f"This is item {item_id}"}
