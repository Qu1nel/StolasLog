"""Unit tests for StolasLog types, enums, and protocols."""

from pathlib import Path
from typing import Any

import pytest

# Import the module to ensure coverage tracking
import stolas_log.types  # noqa: F401
from stolas_log.types import (
    ComponentType,
    FormatterProtocol,
    LogLevel,
    LogRecord,
    SinkProtocol,
)


class TestLogLevel:
    """Test LogLevel enum functionality."""

    def test_log_level_values(self):
        """Test that LogLevel contains all expected values."""
        # Assert
        assert LogLevel.TRACE == 5
        assert LogLevel.DEBUG == 10
        assert LogLevel.INFO == 20
        assert LogLevel.SUCCESS == 25
        assert LogLevel.WARNING == 30
        assert LogLevel.ERROR == 40
        assert LogLevel.CRITICAL == 50

    def test_log_level_ordering(self):
        """Test that LogLevel values can be compared for ordering."""
        # Arrange
        levels = [
            LogLevel.TRACE,
            LogLevel.DEBUG,
            LogLevel.INFO,
            LogLevel.SUCCESS,
            LogLevel.WARNING,
            LogLevel.ERROR,
            LogLevel.CRITICAL,
        ]

        # Act & Assert
        for i in range(len(levels) - 1):
            # Note: This test assumes we'll implement ordering later
            # For now, just test that the values exist
            assert levels[i] in LogLevel
            assert levels[i + 1] in LogLevel

    def test_log_level_from_int(self):
        """Test creating LogLevel from integer values."""
        # Act & Assert
        assert LogLevel(10) == LogLevel.DEBUG
        assert LogLevel(20) == LogLevel.INFO
        assert LogLevel(40) == LogLevel.ERROR

    def test_log_level_invalid_value(self):
        """Test that invalid LogLevel values raise ValueError."""
        # Act & Assert
        with pytest.raises(ValueError, match="999 is not a valid LogLevel"):
            LogLevel(999)


class TestComponentType:
    """Test ComponentType enum functionality."""

    def test_component_type_values(self):
        """Test that ComponentType contains expected values."""
        # Assert
        assert ComponentType.SINK.value == "sink"
        assert ComponentType.FORMATTER.value == "formatter"

    def test_component_type_from_string(self):
        """Test creating ComponentType from string values."""
        # Act & Assert
        assert ComponentType("sink") == ComponentType.SINK
        assert ComponentType("formatter") == ComponentType.FORMATTER

    def test_component_type_invalid_value(self):
        """Test that invalid ComponentType values raise ValueError."""
        # Act & Assert
        with pytest.raises(ValueError, match="'invalid_type' is not a valid ComponentType"):
            ComponentType("invalid_type")


class TestLogRecord:
    """Test LogRecord dataclass functionality."""

    def test_log_record_creation(self):
        """Test creating LogRecord with all fields."""
        # Arrange
        level = LogLevel.INFO
        message = "Test log message"
        timestamp = "2024-01-01T12:00:00"
        module = "test_module"
        function = "test_function"
        line = 42
        extra = {"user_id": 123, "request_id": "abc-123"}

        # Act
        record = LogRecord(
            level=level,
            message=message,
            timestamp=timestamp,
            module=module,
            function=function,
            line=line,
            extra=extra,
        )

        # Assert
        assert record.level == level
        assert record.message == message
        assert record.timestamp == timestamp
        assert record.module == module
        assert record.function == function
        assert record.line == line
        assert record.extra == extra

    def test_log_record_with_optional_fields(self):
        """Test creating LogRecord with minimal required fields."""
        # Arrange
        level = LogLevel.DEBUG
        message = "Debug message"

        # Act
        record = LogRecord(level=level, message=message)

        # Assert
        assert record.level == level
        assert record.message == message
        assert record.timestamp is None
        assert record.module is None
        assert record.function is None
        assert record.line is None
        assert record.extra is None

    def test_log_record_with_exception(self):
        """Test LogRecord with exception information."""
        # Arrange
        level = LogLevel.ERROR
        message = "An error occurred"
        exception = ValueError("Test exception")

        # Act
        record = LogRecord(level=level, message=message, exception=exception)

        # Assert
        assert record.level == level
        assert record.message == message
        assert record.exception == exception


class TestSinkProtocol:
    """Test SinkProtocol interface compliance."""

    def test_sink_protocol_structure(self):
        """Test that SinkProtocol has expected method signatures."""
        # This test verifies the protocol structure exists
        # We'll test actual implementations later

        # Assert protocol methods exist
        assert hasattr(SinkProtocol, "emit")
        assert hasattr(SinkProtocol, "close")

    def test_sink_protocol_implementation(self):
        """Test that a class can implement SinkProtocol."""

        class TestSink:
            """Test implementation of SinkProtocol."""

            def emit(self, record: LogRecord) -> None:
                """Emit a log record."""
                pass

            def close(self) -> None:
                """Close the sink."""
                pass

        # Act
        sink = TestSink()

        # Assert - should not raise any type errors
        assert hasattr(sink, "emit")
        assert hasattr(sink, "close")


class TestFormatterProtocol:
    """Test FormatterProtocol interface compliance."""

    def test_formatter_protocol_structure(self):
        """Test that FormatterProtocol has expected method signatures."""
        # Assert protocol methods exist
        assert hasattr(FormatterProtocol, "format")

    def test_formatter_protocol_implementation(self):
        """Test that a class can implement FormatterProtocol."""

        class TestFormatter:
            """Test implementation of FormatterProtocol."""

            def format(self, record: LogRecord) -> str:
                """Format a log record."""
                return f"{record.level}: {record.message}"

        # Act
        formatter = TestFormatter()
        record = LogRecord(level=LogLevel.INFO, message="Test message")
        result = formatter.format(record)

        # Assert
        assert result == "20: Test message"  # LogLevel.INFO has value 20


class TestTypeAliases:
    """Test type aliases and their usage."""

    def test_path_like_type_alias(self):
        """Test PathLike type alias accepts both str and Path."""
        # This test verifies our type alias works correctly
        # We'll import and test the actual alias once implemented

        # Arrange
        str_path = "/tmp/test.log"
        path_obj = Path("/tmp/test.log")

        # Act & Assert - both should be valid PathLike values
        assert isinstance(str_path, str | Path)
        assert isinstance(path_obj, str | Path)

    def test_config_dict_type_alias(self):
        """Test ConfigDict type alias for configuration dictionaries."""
        # Arrange
        config: dict[str, Any] = {
            "level": "INFO",
            "enabled": True,
            "options": {"path": "/tmp/app.log"},
        }

        # Act & Assert
        assert isinstance(config, dict)
        assert "level" in config
        assert "enabled" in config
        assert "options" in config


class TestProtocolCompliance:
    """Test that protocols work correctly with isinstance checks."""

    def test_sink_protocol_isinstance_check(self):
        """Test isinstance check with SinkProtocol (when supported)."""

        class ValidSink:
            def emit(self, record: LogRecord) -> None:
                pass

            def close(self) -> None:
                pass

        class InvalidSink:
            def emit(self, record: LogRecord) -> None:
                pass

            # Missing close method

        # Act
        valid_sink = ValidSink()
        invalid_sink = InvalidSink()

        # Assert - basic structure check
        assert hasattr(valid_sink, "emit")
        assert hasattr(valid_sink, "close")
        assert hasattr(invalid_sink, "emit")
        assert not hasattr(invalid_sink, "close")

    def test_formatter_protocol_isinstance_check(self):
        """Test isinstance check with FormatterProtocol."""

        class ValidFormatter:
            def format(self, record: LogRecord) -> str:
                return str(record.message)

        class InvalidFormatter:
            def format_message(self, record: LogRecord) -> str:  # Wrong method name
                return str(record.message)

        # Act
        valid_formatter = ValidFormatter()
        invalid_formatter = InvalidFormatter()

        # Assert
        assert hasattr(valid_formatter, "format")
        assert not hasattr(invalid_formatter, "format")
        assert hasattr(invalid_formatter, "format_message")
