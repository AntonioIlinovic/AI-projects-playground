# AI Projects Directory

This directory contains individual AI projects, each with its own isolated uv environment.

## Creating a New Project

### Quick Start (Recommended)
```bash
# Copy the template
cp -r project-template my-new-project
cd my-new-project

# Set up environment
cp .env.example .env
# Edit .env with your configuration

# Initialize uv
uv init
uv sync

# Install dependencies
uv add python-dotenv openai  # example packages
```

### Manual Setup
```bash
# Create project directory
mkdir my-new-project
cd my-new-project

# Create basic structure
mkdir src
touch src/main.py
touch .env.example
touch README.md

# Initialize uv
uv init
```

## Project Management

### Working with Projects
```bash
# Navigate to project
cd projects/my-project

# Run commands in environment
uv run python src/main.py
uv run jupyter notebook

# Install packages
uv add pandas numpy
uv add --dev pytest black

# List installed packages
uv pip list
```

### Environment Management
```bash
# Activate environment (optional)
source .venv/bin/activate

# Deactivate when done
deactivate

# Recreate environment
uv sync --reinstall
```

## Best Practices

1. **Always copy the template** - Start with `project-template` for consistency
2. **Use .env files** - Keep secrets out of code, use `.env.example` as template
3. **Isolate dependencies** - Each project should have its own `pyproject.toml`
4. **Document your project** - Update README.md with project-specific info
5. **Version control** - Commit `.env.example` but not `.env`

## Project Examples

Browse existing projects in this directory to see different AI implementations:
- Language models
- Computer vision
- Data analysis
- Automation scripts
- And more!

Each project is self-contained and can be run independently.
