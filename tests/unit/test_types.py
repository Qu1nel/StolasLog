"""Unit tests for stolas_log.types module."""

from stolas_log.exceptions import ComponentError, ConfigurationError, StolasLogError
from stolas_log.types import ComponentType, LogLevel, SinkType


class TestLogLevel:
    """Test LogLevel enum and type alias."""

    def test_log_level_enum_values(self):
        """Test that LogLevel enum contains all expected values."""
        expected_levels = {"TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"}
        actual_levels = {level.name for level in LogLevel}
        assert actual_levels == expected_levels

    def test_log_level_ordering(self):
        """Test that LogLevel enum values have correct ordering."""
        assert LogLevel.TRACE < LogLevel.DEBUG
        assert LogLevel.DEBUG < LogLevel.INFO
        assert LogLevel.INFO < LogLevel.SUCCESS
        assert LogLevel.SUCCESS < LogLevel.WARNING
        assert LogLevel.WARNING < LogLevel.ERROR
        assert LogLevel.ERROR < LogLevel.CRITICAL

    def test_log_level_string_conversion(self):
        """Test LogLevel string representation."""
        assert LogLevel.INFO.name == "INFO"
        assert LogLevel.INFO.value == 20


class TestSinkType:
    """Test SinkType enum."""

    def test_sink_type_values(self):
        """Test that SinkType contains expected sink types."""
        expected_types = {"console_plain", "console_rich", "file_text", "stderr_console"}
        actual_types = {sink_type.value for sink_type in SinkType}
        assert actual_types == expected_types


class TestComponentType:
    """Test ComponentType enum."""

    def test_component_type_values(self):
        """Test that ComponentType contains expected component types."""
        expected_types = {"sink", "formatter"}
        actual_types = {comp_type.value for comp_type in ComponentType}
        assert actual_types == expected_types


class TestExceptionHierarchy:
    """Test exception hierarchy and behavior."""

    def test_stolas_log_error_is_base_exception(self):
        """Test that StolasLogError is the base exception."""
        error = StolasLogError("Test error")
        assert isinstance(error, Exception)
        assert str(error) == "Test error"

    def test_configuration_error_inheritance(self):
        """Test ConfigurationError inherits from StolasLogError."""
        error = ConfigurationError("Config error")
        assert isinstance(error, StolasLogError)
        assert isinstance(error, Exception)

    def test_component_error_inheritance(self):
        """Test ComponentError inherits from StolasLogError."""
        error = ComponentError("Component error")
        assert isinstance(error, StolasLogError)
        assert isinstance(error, Exception)

    def test_exception_with_context(self):
        """Test exceptions can carry additional context."""
        error = ConfigurationError("Invalid level", context={"level": "INVALID", "valid_levels": ["INFO", "DEBUG"]})
        assert hasattr(error, "context")
        assert error.context["level"] == "INVALID"
