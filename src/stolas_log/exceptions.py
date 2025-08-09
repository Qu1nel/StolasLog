"""Exception hierarchy for StolasLog.

This module defines all custom exceptions used throughout the StolasLog system,
providing a clear hierarchy for different types of errors that can occur.
"""

from typing import Any

__all__ = [
    "StolasLogError",
    "ConfigurationError",
    "ComponentError",
    "SinkError",
    "FormatterError",
]


class StolasLogError(Exception):
    """Base exception for all StolasLog errors.

    All custom exceptions in StolasLog inherit from this base class.
    Provides optional context information for better error diagnostics.
    """

    def __init__(self, message: str, *, context: dict[str, Any] | None = None) -> None:
        """Initialize the exception with message and optional context.

        Args:
            message: Human-readable error message.
            context: Optional dictionary with additional error context.
        """
        super().__init__(message)
        self.context: dict[str, Any] = context or {}


class ConfigurationError(StolasLogError):
    """Exception raised for configuration-related errors.

    This exception is raised when there are issues with logger configuration,
    such as invalid parameter values, conflicting settings, or validation failures.
    """

    pass


class ComponentError(StolasLogError):
    """Exception raised for component-related errors.

    Base class for all errors related to StolasLog components (sinks, formatters).
    Used when components fail to initialize, register, or operate correctly.
    """

    pass


class SinkError(ComponentError):
    """Exception raised for sink-specific errors.

    This exception is raised when sinks fail to emit log records,
    encounter I/O errors, or have configuration issues.
    """

    pass


class FormatterError(ComponentError):
    """Exception raised for formatter-specific errors.

    This exception is raised when formatters fail to format log records
    or encounter issues with format strings or templates.
    """

    pass
