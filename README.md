# FastAPI Test Project

A FastAPI Python 3 project with GitHub Actions CI performing static code analysis using modern Python tools.

## 🚀 Features

- **FastAPI Application**: Modern, fast web framework for building APIs
- **Static Code Analysis**: Automated code quality checks using:
  - **Ruff**: Fast Python linter (replaces Flake8, isort, and more)
  - **Black**: Uncompromising code formatter
  - **MyPy**: Static type checker
- **GitHub Actions CI**: Automated testing on Python 3.10, 3.11, and 3.12
- **Type Hints**: Full type annotations for better code quality

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Pelleplutt/fastapi-test.git
cd fastapi-test
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools
```

## 🏃 Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
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

## 🔄 GitHub Actions CI

The CI pipeline automatically runs on:
- Push to `main`, `master`, or `develop` branches
- Pull requests to these branches
- Manual workflow dispatch

### CI Jobs

1. **Static Analysis** (runs on Python 3.10, 3.11, 3.12):
   - Ruff linting
   - Black formatting check
   - MyPy type checking
   - Unit tests (if available)

2. **API Test**:
   - Verifies FastAPI application starts successfully

## 🛠️ Development

### Project Structure
```
fastapi-test/
├── main.py                 # FastAPI application
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
├── pyproject.toml         # Tool configurations
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
