"""Pydantic models for StolasLog configuration.

This module defines all configuration models used throughout the StolasLog system,
providing type-safe configuration with validation and serialization capabilities.
"""

from typing import Any

from pydantic import BaseModel, Field

from stolas_log.types import ComponentType, LogLevel, LogLevelType

__all__ = [
    "ComponentMetadata",
    "SinkConfig",
    "FormatterConfig",
    "LoggerConfig",
]


class ComponentMetadata(BaseModel):
    """Metadata for StolasLog components (sinks, formatters, etc.).

    Contains information about component identity, version, and type
    for registration and management in the plugin system.
    """

    name: str = Field(..., min_length=1, description="Unique name of the component")
    version: str = Field(..., min_length=1, description="Version string (e.g., '1.0.0')")
    component_type: ComponentType = Field(..., description="Type of component (sink or formatter)")
    author: str = Field(default="Unknown", description="Author or organization name")
    description: str | None = Field(default=None, description="Optional description of the component")

    model_config = {
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "extra": "forbid",
    }


class SinkConfig(BaseModel):
    """Configuration for a sink component.

    Defines how a sink should be configured, including its name,
    log level, format, and any sink-specific options.
    """

    name: str = Field(..., min_length=1, description="Name of the sink to use")
    level: LogLevelType | None = Field(default=None, description="Minimum log level for this sink")
    format: str | None = Field(default=None, description="Custom format string for this sink")
    enabled: bool = Field(default=True, description="Whether this sink is enabled")
    options: dict[str, Any] = Field(default_factory=dict, description="Sink-specific configuration options")

    model_config = {
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "extra": "forbid",
    }


class FormatterConfig(BaseModel):
    """Configuration for a formatter component.

    Defines how a formatter should be configured, including its name,
    format string, and any formatter-specific options.
    """

    name: str = Field(..., min_length=1, description="Name of the formatter to use")
    format_string: str | None = Field(default=None, description="Format template string")
    options: dict[str, Any] = Field(default_factory=dict, description="Formatter-specific configuration options")

    model_config = {
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "extra": "forbid",
    }


class LoggerConfig(BaseModel):
    """Main configuration for the StolasLog logger.

    Contains all settings for the logger including global level,
    backtrace/diagnose settings, and lists of sinks and formatters.
    """

    level: LogLevelType = Field(default=LogLevel.INFO, description="Global minimum log level")
    enable_backtrace: bool = Field(default=True, description="Enable detailed backtraces for exceptions")
    diagnose: bool = Field(default=False, description="Enable diagnostic information in exceptions")
    sinks: list[SinkConfig] = Field(default_factory=list, description="List of sink configurations")
    formatters: list[FormatterConfig] = Field(default_factory=list, description="List of formatter configurations")

    model_config = {
        "str_strip_whitespace": True,
        "validate_assignment": True,
        "extra": "forbid",
    }
