# StolasLog 🦉

<p align="center">
  <a href="https://github.com/Qu1nel/StolasLog/actions/workflows/tests.yml"><img alt="CI Status" src="https://github.com/Qu1nel/StolasLog/actions/workflows/tests.yml/badge.svg"></a>
  <a href="https://app.codecov.io/gh/Qu1nel/StolasLog"><img alt="Coverage" src="https://codecov.io/gh/Qu1nel/StolasLog/branch/main/graph/badge.svg"></a>
  <a href="https://pypi.org/project/stolas-log/"><img alt="PyPI" src="https://img.shields.io/pypi/v/stolas-log"></a>
  <a href="https://github.com/Qu1nel/StolasLog/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

<p align="center">
  <em>An elegant, powerful, and highly configurable logging framework for Python, built on Loguru, Pydantic, and Rich.</em>
</p>

<!-- end-of-readme-intro -->

## Key Features

* **Simple by Default, Powerful when Needed:** Start logging in one line with `logger.setup()`, or configure every
  detail with a flexible, multi-layered API.
* **Rich & Beautiful Output:** Powered by `rich` for beautiful, readable, and structured console logs with themes and
  pretty-printing.
* **Strictly Typed Configuration:** Powered by `Pydantic` for reliable, validated, and self-documenting configuration
  from `kwargs`, environment variables, or `pyproject.toml`.
* **Extensible by Design:** A simple but powerful plugin system based on decorators and Python Protocols to easily
  create your own custom sinks and formatters.
* **Ready for Production:** Built-in support for file rotation, JSON logging, asynchronous operations, and flawless
  performance on Windows, Linux, and WSL.

## Installation

```bash
pip install stolas-log
```

## Quick Start

```python
from stolas_log import logger, LogLevel

# Get beautiful, structured logs with zero configuration (uses rich by default)
logger.info("Starting the application...")
logger.warning("Something might be wrong here.")

# --- Or ---

# Configure everything to your liking with a simple, powerful API
logger.setup(
    level=LogLevel.DEBUG,
    use_rich=True,
    log_file_path="app.log",
    rotation="10 MB",
    retention="5 days"
)

logger.debug("This is a debug message for the console and file.")

# Log complex objects with beautiful formatting
my_data = {"user": "Stolas", "permissions": ["read", "write"], "id": 72}
logger.info("User data retrieved:", data=my_data)
```

For full documentation, visit [stolaslog.readthedocs.io](https://stolaslog.readthedocs.io/en/latest/).

---
*This project is currently in early development.*