"""StolasLog - An elegant, powerful, and highly configurable logging framework for Python.

Built on Loguru, Pydantic, and Rich, StolasLog provides a simple API for basic use cases
while offering powerful extensibility through a plugin system for advanced scenarios.
"""

from importlib.metadata import version

from stolas_log.exceptions import (
    ComponentError,
    ConfigurationError,
    FormatterError,
    SinkError,
    StolasLogError,
)
from stolas_log.types import (
    ComponentType,
    FormatterProtocol,
    LogLevel,
    LogRecord,
    SinkProtocol,
)

__version__ = version("stolas-log")

__all__ = [
    # Core types and enums
    "LogLevel",
    "ComponentType",
    "LogRecord",
    # Protocols for extensibility
    "SinkProtocol",
    "FormatterProtocol",
    # Exception hierarchy
    "StolasLogError",
    "ConfigurationError",
    "ComponentError",
    "SinkError",
    "FormatterError",
    # Version
    "__version__",
]
