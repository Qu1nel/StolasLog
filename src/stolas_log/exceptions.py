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
    """Base exception for all StolasLog-related errors.

    All other StolasLog exceptions inherit from this base class,
    allowing for easy catching of any StolasLog-specific error.
    """

    def __init__(self, message: str, **kwargs: Any) -> None:
        """Initialize the exception with a message and optional context.

        Args:
            message: Human-readable error message.
            **kwargs: Additional context information stored as attributes.
        """
        super().__init__(message)
        # Store additional context as instance attributes
        for key, value in kwargs.items():
            setattr(self, key, value)


class ConfigurationError(StolasLogError):
    """Exception raised when there are configuration-related errors.

    This includes invalid configuration values, missing required settings,
    or conflicts between configuration options.
    """

    def __init__(self, message: str, field: str | None = None, value: Any | None = None, **kwargs: Any) -> None:
        """Initialize configuration error with field context.

        Args:
            message: Human-readable error message.
            field: Name of the configuration field that caused the error.
            value: The invalid value that was provided.
            **kwargs: Additional context information.
        """
        super().__init__(message, field=field, value=value, **kwargs)


class ComponentError(StolasLogError):
    """Exception raised when there are component-related errors.

    This includes errors during component registration, initialization,
    or operation of sinks, formatters, and other components.
    """

    def __init__(self, message: str, component_name: str | None = None, **kwargs: Any) -> None:
        """Initialize component error with component context.

        Args:
            message: Human-readable error message.
            component_name: Name of the component that caused the error.
            **kwargs: Additional context information.
        """
        super().__init__(message, component_name=component_name, **kwargs)


class SinkError(ComponentError):
    """Exception raised when there are sink-specific errors.

    This includes errors during sink initialization, log emission,
    or resource management within sink components.
    """

    def __init__(self, message: str, sink_name: str | None = None, **kwargs: Any) -> None:
        """Initialize sink error with sink context.

        Args:
            message: Human-readable error message.
            sink_name: Name of the sink that caused the error.
            **kwargs: Additional context information (e.g., file_path).
        """
        super().__init__(message, component_name=sink_name, sink_name=sink_name, **kwargs)


class FormatterError(ComponentError):
    """Exception raised when there are formatter-specific errors.

    This includes errors during formatter initialization, log formatting,
    or template processing within formatter components.
    """

    def __init__(self, message: str, formatter_name: str | None = None, **kwargs: Any) -> None:
        """Initialize formatter error with formatter context.

        Args:
            message: Human-readable error message.
            formatter_name: Name of the formatter that caused the error.
            **kwargs: Additional context information.
        """
        super().__init__(message, component_name=formatter_name, **kwargs)
