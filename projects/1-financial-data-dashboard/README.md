# Project Name

Brief description of your AI project.

## Setup

1. Copy `.env.example` to `.env` and fill in your configuration
2. Initialize uv environment:
```bash
uv init
uv sync
```

3. Install dependencies:
```bash
uv add <package-name>
```

## Usage

```bash
# Run the main script
uv run python src/main.py

# Or activate environment first
source .venv/bin/activate
python src/main.py
```

## Project Structure

```
project-name/
├── .env              # Environment variables (create from .env.example)
├── .env.example      # Template for environment variables
├── pyproject.toml    # uv project configuration
├── README.md         # Project documentation
└── src/              # Source code
    └── main.py       # Main entry point
```
