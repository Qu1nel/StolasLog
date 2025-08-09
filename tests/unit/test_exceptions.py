"""Unit tests for StolasLog exception hierarchy."""

import pytest

# Import the module to ensure coverage tracking
import stolas_log.exceptions  # noqa: F401
from stolas_log.exceptions import (
    ComponentError,
    ConfigurationError,
    FormatterError,
    SinkError,
    StolasLogError,
)


class TestExceptionHierarchy:
    """Test the exception hierarchy structure."""

    def test_base_exception_inheritance(self):
        """Test that all exceptions inherit from StolasLogError."""
        # Arrange & Act
        config_error = ConfigurationError("Config error")
        component_error = ComponentError("Component error")
        sink_error = SinkError("Sink error")
        formatter_error = FormatterError("Formatter error")

        # Assert
        assert isinstance(config_error, StolasLogError)
        assert isinstance(component_error, StolasLogError)
        assert isinstance(sink_error, ComponentError)  # SinkError inherits from ComponentError
        assert isinstance(formatter_error, ComponentError)  # FormatterError inherits from ComponentError

    def test_stolas_log_error_creation(self):
        """Test StolasLogError can be created with message."""
        # Arrange
        message = "Base StolasLog error occurred"

        # Act
        error = StolasLogError(message)

        # Assert
        assert str(error) == message
        assert isinstance(error, Exception)

    def test_configuration_error_creation(self):
        """Test ConfigurationError creation and message handling."""
        # Arrange
        message = "Invalid configuration provided"

        # Act
        error = ConfigurationError(message)

        # Assert
        assert str(error) == message
        assert isinstance(error, StolasLogError)

    def test_component_error_creation(self):
        """Test ComponentError creation and message handling."""
        # Arrange
        message = "Component failed to initialize"

        # Act
        error = ComponentError(message)

        # Assert
        assert str(error) == message
        assert isinstance(error, StolasLogError)

    def test_sink_error_creation(self):
        """Test SinkError creation and inheritance."""
        # Arrange
        message = "Sink failed to emit log record"

        # Act
        error = SinkError(message)

        # Assert
        assert str(error) == message
        assert isinstance(error, ComponentError)
        assert isinstance(error, StolasLogError)

    def test_formatter_error_creation(self):
        """Test FormatterError creation and inheritance."""
        # Arrange
        message = "Formatter failed to format log record"

        # Act
        error = FormatterError(message)

        # Assert
        assert str(error) == message
        assert isinstance(error, ComponentError)
        assert isinstance(error, StolasLogError)


class TestExceptionWithContext:
    """Test exceptions with additional context information."""

    def test_configuration_error_with_field_context(self):
        """Test ConfigurationError with field-specific context."""
        # Arrange
        message = "Invalid log level"
        field = "level"
        value = "INVALID_LEVEL"

        # Act
        error = ConfigurationError(message, field=field, value=value)

        # Assert
        assert str(error) == message
        assert hasattr(error, "field")
        assert hasattr(error, "value")
        assert error.field == field
        assert error.value == value

    def test_component_error_with_component_name(self):
        """Test ComponentError with component name context."""
        # Arrange
        message = "Component initialization failed"
        component_name = "RichConsoleSink"

        # Act
        error = ComponentError(message, component_name=component_name)

        # Assert
        assert str(error) == message
        assert hasattr(error, "component_name")
        assert error.component_name == component_name

    def test_sink_error_with_sink_context(self):
        """Test SinkError with sink-specific context."""
        # Arrange
        message = "Failed to write to file"
        sink_name = "FileTextSink"
        file_path = "/tmp/app.log"

        # Act
        error = SinkError(message, sink_name=sink_name, file_path=file_path)

        # Assert
        assert str(error) == message
        assert hasattr(error, "sink_name")
        assert hasattr(error, "file_path")
        assert error.sink_name == sink_name
        assert error.file_path == file_path


class TestExceptionRaising:
    """Test that exceptions can be properly raised and caught."""

    def test_raise_and_catch_stolas_log_error(self):
        """Test raising and catching base StolasLogError."""
        # Arrange
        message = "Base error"

        # Act & Assert
        with pytest.raises(StolasLogError) as exc_info:
            raise StolasLogError(message)

        assert str(exc_info.value) == message

    def test_raise_and_catch_configuration_error(self):
        """Test raising and catching ConfigurationError."""
        # Arrange
        message = "Configuration is invalid"

        # Act & Assert
        with pytest.raises(ConfigurationError) as exc_info:
            raise ConfigurationError(message)

        assert str(exc_info.value) == message

    def test_catch_component_error_as_base_error(self):
        """Test that ComponentError can be caught as StolasLogError."""
        # Arrange
        message = "Component error"

        # Act & Assert
        with pytest.raises(StolasLogError) as exc_info:
            raise ComponentError(message)

        assert isinstance(exc_info.value, ComponentError)
        assert str(exc_info.value) == message

    def test_catch_sink_error_as_component_error(self):
        """Test that SinkError can be caught as ComponentError."""
        # Arrange
        message = "Sink error"

        # Act & Assert
        with pytest.raises(ComponentError) as exc_info:
            raise SinkError(message)

        assert isinstance(exc_info.value, SinkError)
        assert str(exc_info.value) == message
