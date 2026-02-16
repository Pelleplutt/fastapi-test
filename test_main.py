"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root() -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Test API"}


def test_health_check() -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_item_success() -> None:
    """Test creating an item successfully."""
    item_data = {"name": "Test Item", "price": 10.0, "tax": 1.5}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["total_price"] == 11.5


def test_create_item_without_tax() -> None:
    """Test creating an item without tax."""
    item_data = {"name": "Test Item", "price": 10.0}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["total_price"] == 10.0


def test_create_item_negative_price() -> None:
    """Test creating an item with negative price should fail."""
    item_data = {"name": "Test Item", "price": -10.0}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 400
    assert "Price cannot be negative" in response.json()["detail"]


def test_read_item() -> None:
    """Test reading an item by ID."""
    response = client.get("/items/42")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert "This is item 42" in data["message"]


def test_openapi_schema() -> None:
    """Test that OpenAPI schema is accessible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"] == "FastAPI Test API"
    assert schema["info"]["version"] == "1.0.0"
