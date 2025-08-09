"""Unit tests for stolas_log.exceptions module."""

from stolas_log.exceptions import ComponentError, ConfigurationError, FormatterError, SinkError, StolasLogError


class TestStolasLogError:
    """Test base StolasLogError class."""

    def test_basic_error_creation(self):
        """Test basic error creation with message."""
        error = StolasLogError("Test message")
        assert str(error) == "Test message"
        assert error.args == ("Test message",)

    def test_error_with_context(self):
        """Test error creation with additional context."""
        context = {"component": "test", "operation": "init"}
        error = StolasLogError("Test message", context=context)
        assert str(error) == "Test message"
        assert error.context == context

    def test_error_without_context(self):
        """Test error creation without context."""
        error = StolasLogError("Test message")
        assert error.context == {}


class TestConfigurationError:
    """Test ConfigurationError class."""

    def test_configuration_error_inheritance(self):
        """Test ConfigurationError inherits from StolasLogError."""
        error = ConfigurationError("Config error")
        assert isinstance(error, StolasLogError)
        assert isinstance(error, Exception)

    def test_configuration_error_with_details(self):
        """Test ConfigurationError with validation details."""
        details = {"field": "level", "value": "INVALID", "valid_options": ["DEBUG", "INFO", "WARNING", "ERROR"]}
        error = ConfigurationError("Invalid log level", context=details)
        assert "Invalid log level" in str(error)
        assert error.context["field"] == "level"


class TestComponentError:
    """Test ComponentError class."""

    def test_component_error_inheritance(self):
        """Test ComponentError inherits from StolasLogError."""
        error = ComponentError("Component error")
        assert isinstance(error, StolasLogError)

    def test_component_error_with_component_info(self):
        """Test ComponentError with component information."""
        context = {"component_name": "test_sink", "component_type": "sink", "operation": "emit"}
        error = ComponentError("Component failed", context=context)
        assert error.context["component_name"] == "test_sink"


class TestSinkError:
    """Test SinkError class."""

    def test_sink_error_inheritance(self):
        """Test SinkError inherits from ComponentError."""
        error = SinkError("Sink error")
        assert isinstance(error, ComponentError)
        assert isinstance(error, StolasLogError)


class TestFormatterError:
    """Test FormatterError class."""

    def test_formatter_error_inheritance(self):
        """Test FormatterError inherits from ComponentError."""
        error = FormatterError("Formatter error")
        assert isinstance(error, ComponentError)
        assert isinstance(error, StolasLogError)
