"""Core types, enums, and type aliases for StolasLog.

This module defines all fundamental types used throughout the StolasLog system,
including log levels, component types, and type aliases for better type safety.
"""

from dataclasses import dataclass
from enum import Enum, IntEnum
from pathlib import Path
from typing import Any, Protocol, TypeAlias

__all__ = [
    "LogLevel",
    "SinkType",
    "ComponentType",
    "LogLevelType",
    "PathType",
    "LogRecord",
    "SinkProtocol",
    "FormatterProtocol",
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


@dataclass
class LogRecord:
    """Represents a single log record with all associated metadata.

    This dataclass contains all information about a log entry, including
    the message, level, timing, source location, and any additional context.
    """

    level: LogLevel
    message: str
    timestamp: str | None = None
    module: str | None = None
    function: str | None = None
    line: int | None = None
    extra: dict[str, Any] | None = None
    exception: Exception | None = None


class SinkProtocol(Protocol):
    """Protocol defining the interface for sink components.

    All sink implementations (both built-in and external plugins) must
    implement this protocol to be compatible with the StolasLog system.
    """

    def emit(self, record: LogRecord) -> None:
        """Emit a log record to the sink's destination.

        Args:
            record: The log record to emit.
        """
        ...

    def close(self) -> None:
        """Close the sink and release any resources.

        This method should be called when the sink is no longer needed
        to ensure proper cleanup of resources like file handles or network connections.
        """
        ...


class FormatterProtocol(Protocol):
    """Protocol defining the interface for formatter components.

    All formatter implementations must implement this protocol to be
    compatible with the StolasLog system.
    """

    def format(self, record: LogRecord) -> str:
        """Format a log record into a string representation.

        Args:
            record: The log record to format.

        Returns:
            The formatted log message as a string.
        """
        ...


# Type aliases for better type hints and documentation
LogLevelType: TypeAlias = LogLevel | str
"""Type alias for log level that accepts both enum and string values."""

PathType: TypeAlias = str | Path
"""Type alias for file paths that accepts both string and Path objects."""
