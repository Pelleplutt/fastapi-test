# FastAPI Test Project

A FastAPI Python 3 project with GitHub Actions CI performing static code analysis using modern Python tools, containerized with Docker.

## 🚀 Features

- **FastAPI Application**: Modern, fast web framework for building APIs
- **Static Code Analysis**: Automated code quality checks using:
  - **Ruff**: Fast Python linter (replaces Flake8, isort, and more)
  - **Black**: Uncompromising code formatter
  - **MyPy**: Static type checker
- **uv Package Manager**: Fast Python package installer and resolver
- **Docker Support**: Containerized application for easy deployment
- **GitHub Actions CI**: Automated testing on Python 3.12
- **Type Hints**: Full type annotations for better code quality

## 📋 Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Docker (optional, for containerized deployment)

## 🔧 Installation

### Option 1: Local Development with uv

1. Clone the repository:
```bash
git clone https://github.com/Pelleplutt/fastapi-test.git
cd fastapi-test
```

2. Install uv (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt  # For development tools
```

### Option 2: Docker

1. Clone the repository:
```bash
git clone https://github.com/Pelleplutt/fastapi-test.git
cd fastapi-test
```

2. Build the Docker image:
```bash
docker build -t fastapi-test .
```

3. Run the container:
```bash
docker run -p 8000:8000 fastapi-test
```

## 🏃 Running the Application

### Local Development
Start the FastAPI server:
```bash
uvicorn main:app --reload
```

### Docker
```bash
docker run -p 8000:8000 fastapi-test
```

The API will be available at: `http://localhost:8000`

### Interactive API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check endpoint
- `POST /items/` - Create a new item with price calculation
- `GET /items/{item_id}` - Retrieve item by ID

### Example Request

```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Example Item", "price": 10.5, "tax": 1.5}'
```

## 🔍 Static Code Analysis

Run static analysis tools locally:

### Ruff (Linter)
```bash
ruff check .
ruff check . --fix  # Auto-fix issues
```

### Black (Formatter)
```bash
black .  # Format all files
black --check .  # Check without modifying
```

### MyPy (Type Checker)
```bash
mypy main.py
```

### Run All Checks
```bash
ruff check . && black --check . && mypy main.py
```

## 🐳 Docker

### Building the Image
```bash
docker build -t fastapi-test .
```

### Running the Container
```bash
docker run -d -p 8000:8000 --name fastapi-test fastapi-test
```

### Stopping the Container
```bash
docker stop fastapi-test
docker rm fastapi-test
```

## 🔄 GitHub Actions CI

The CI pipeline automatically runs on:
- Push to `main`, `master`, or `develop` branches
- Pull requests to these branches
- Manual workflow dispatch

### CI Jobs

1. **Static Analysis** (Python 3.12):
   - Installs dependencies using uv
   - Ruff linting
   - Black formatting check
   - MyPy type checking
   - Unit tests

2. **API Test**:
   - Verifies FastAPI application starts successfully

3. **Docker Build**:
   - Builds Docker image
   - Tests container startup and health check

## 🛠️ Development

### Project Structure
```
fastapi-test/
├── main.py                 # FastAPI application
├── test_main.py            # Test suite
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── pyproject.toml         # Tool configurations
├── Dockerfile             # Docker configuration
├── .dockerignore          # Docker ignore rules
├── .gitignore             # Git ignore rules
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions workflow
└── README.md              # This file
```

### Code Style

This project follows:
- **PEP 8** style guide (enforced by Ruff)
- **Black** formatting (line length: 100)
- **Type hints** for all functions (checked by MyPy)

## 📝 License

This is a test project for learning FastAPI and GitHub Actions CI.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all static analysis checks pass
5. Submit a pull request
