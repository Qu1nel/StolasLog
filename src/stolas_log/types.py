"""Core types, enums, and type aliases for StolasLog.

This module defines all fundamental types used throughout the StolasLog system,
including log levels, component types, and type aliases for better type safety.
"""

from enum import Enum, IntEnum
from pathlib import Path
from typing import TypeAlias

__all__ = [
    "LogLevel",
    "SinkType",
    "ComponentType",
    "LogLevelType",
    "PathType",
]


class LogLevel(IntEnum):
    """Enumeration of log levels with integer values for ordering.

    Uses the same levels as loguru with proper ordering for comparison operations.
    Lower values indicate more verbose logging levels.
    """

    TRACE = 5
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class SinkType(Enum):
    """Enumeration of built-in sink types.

    Defines all sink types that are provided out-of-the-box with StolasLog.
    """

    CONSOLE_PLAIN = "console_plain"
    CONSOLE_RICH = "console_rich"
    FILE_TEXT = "file_text"
    STDERR_CONSOLE = "stderr_console"


class ComponentType(Enum):
    """Enumeration of component types for the plugin system.

    Used to categorize different types of components that can be registered
    with the StolasLog plugin system.
    """

    SINK = "sink"
    FORMATTER = "formatter"


# Type aliases for better type hints and documentation
LogLevelType: TypeAlias = LogLevel | str
"""Type alias for log level that accepts both enum and string values."""

PathType: TypeAlias = str | Path
"""Type alias for file paths that accepts both string and Path objects."""
