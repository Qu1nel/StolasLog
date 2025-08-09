"""Unit tests for StolasLog Pydantic configuration models."""

from pathlib import Path

import pytest
from pydantic import ValidationError

# Import the module to ensure coverage tracking
import stolas_log.configs.models  # noqa: F401
from stolas_log.configs.models import (
    ComponentMetadata,
    FormatterConfig,
    LoggerConfig,
    SinkConfig,
)
from stolas_log.types import ComponentType, LogLevel


class TestComponentMetadata:
    """Test ComponentMetadata model validation and functionality."""

    def test_component_metadata_creation_with_required_fields(self):
        """Test creating ComponentMetadata with only required fields."""
        # Arrange
        name = "TestSink"
        version = "1.0.0"
        component_type = ComponentType.SINK

        # Act
        metadata = ComponentMetadata(
            name=name,
            version=version,
            component_type=component_type,
        )

        # Assert
        assert metadata.name == name
        assert metadata.version == version
        assert metadata.component_type == component_type
        assert metadata.author == "Unknown"  # Default value
        assert metadata.description is None  # Default value

    def test_component_metadata_creation_with_all_fields(self):
        """Test creating ComponentMetadata with all fields."""
        # Arrange
        name = "RichConsoleSink"
        version = "2.1.0"
        component_type = ComponentType.SINK
        author = "StolasLog Team"
        description = "Rich-formatted console output sink"

        # Act
        metadata = ComponentMetadata(
            name=name,
            version=version,
            component_type=component_type,
            author=author,
            description=description,
        )

        # Assert
        assert metadata.name == name
        assert metadata.version == version
        assert metadata.component_type == component_type
        assert metadata.author == author
        assert metadata.description == description

    def test_component_metadata_validation_empty_name(self):
        """Test that empty name raises ValidationError."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            ComponentMetadata(
                name="",
                version="1.0.0",
                component_type=ComponentType.SINK,
            )

        assert "String should have at least 1 character" in str(exc_info.value)

    def test_component_metadata_validation_empty_version(self):
        """Test that empty version raises ValidationError."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            ComponentMetadata(
                name="TestSink",
                version="",
                component_type=ComponentType.SINK,
            )

        assert "String should have at least 1 character" in str(exc_info.value)

    def test_component_metadata_validation_invalid_component_type(self):
        """Test that invalid component_type raises ValidationError."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            ComponentMetadata(
                name="TestSink",
                version="1.0.0",
                component_type="invalid_type",  # type: ignore
            )

        assert "Input should be" in str(exc_info.value)


class TestSinkConfig:
    """Test SinkConfig model validation and functionality."""

    def test_sink_config_creation_minimal(self):
        """Test creating SinkConfig with minimal required fields."""
        # Arrange
        name = "console_plain"

        # Act
        config = SinkConfig(name=name)

        # Assert
        assert config.name == name
        assert config.level is None  # Default
        assert config.format is None  # Default
        assert config.enabled is True  # Default
        assert config.options == {}  # Default

    def test_sink_config_creation_with_all_fields(self):
        """Test creating SinkConfig with all fields."""
        # Arrange
        name = "file_text"
        level = LogLevel.DEBUG
        format_str = "{time} | {level} | {message}"
        enabled = True
        options = {"path": "/tmp/app.log", "encoding": "utf-8"}

        # Act
        config = SinkConfig(
            name=name,
            level=level,
            format=format_str,
            enabled=enabled,
            options=options,
        )

        # Assert
        assert config.name == name
        assert config.level == level
        assert config.format == format_str
        assert config.enabled == enabled
        assert config.options == options

    def test_sink_config_level_from_string(self):
        """Test that level accepts string values."""
        # Arrange & Act
        config = SinkConfig(name="test_sink", level="INFO")

        # Assert
        assert config.level == "INFO"

    def test_sink_config_level_from_enum(self):
        """Test that level accepts LogLevel enum values."""
        # Arrange & Act
        config = SinkConfig(name="test_sink", level=LogLevel.WARNING)

        # Assert
        assert config.level == LogLevel.WARNING

    def test_sink_config_validation_empty_name(self):
        """Test that empty name raises ValidationError."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            SinkConfig(name="")

        assert "String should have at least 1 character" in str(exc_info.value)

    def test_sink_config_options_type_validation(self):
        """Test that options must be a dictionary."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            SinkConfig(name="test_sink", options="invalid")  # type: ignore

        assert "Input should be a valid dictionary" in str(exc_info.value)


class TestFormatterConfig:
    """Test FormatterConfig model validation and functionality."""

    def test_formatter_config_creation_minimal(self):
        """Test creating FormatterConfig with minimal fields."""
        # Arrange
        name = "plain_formatter"

        # Act
        config = FormatterConfig(name=name)

        # Assert
        assert config.name == name
        assert config.format_string is None  # Default
        assert config.options == {}  # Default

    def test_formatter_config_creation_with_all_fields(self):
        """Test creating FormatterConfig with all fields."""
        # Arrange
        name = "rich_formatter"
        format_string = "<green>{time}</green> | <level>{level}</level> | {message}"
        options = {"theme": "monokai", "highlight": True}

        # Act
        config = FormatterConfig(
            name=name,
            format_string=format_string,
            options=options,
        )

        # Assert
        assert config.name == name
        assert config.format_string == format_string
        assert config.options == options

    def test_formatter_config_validation_empty_name(self):
        """Test that empty name raises ValidationError."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            FormatterConfig(name="")

        assert "String should have at least 1 character" in str(exc_info.value)


class TestLoggerConfig:
    """Test LoggerConfig model validation and functionality."""

    def test_logger_config_creation_defaults(self):
        """Test creating LoggerConfig with default values."""
        # Act
        config = LoggerConfig()

        # Assert
        assert config.level == LogLevel.INFO  # Default
        assert config.enable_backtrace is True  # Default
        assert config.diagnose is False  # Default
        assert config.sinks == []  # Default
        assert config.formatters == []  # Default

    def test_logger_config_creation_with_all_fields(self):
        """Test creating LoggerConfig with all fields."""
        # Arrange
        level = LogLevel.DEBUG
        enable_backtrace = False
        diagnose = True
        sinks = [
            SinkConfig(name="console_rich"),
            SinkConfig(name="file_text", options={"path": "app.log"}),
        ]
        formatters = [
            FormatterConfig(name="rich_formatter", options={"theme": "dark"}),
        ]

        # Act
        config = LoggerConfig(
            level=level,
            enable_backtrace=enable_backtrace,
            diagnose=diagnose,
            sinks=sinks,
            formatters=formatters,
        )

        # Assert
        assert config.level == level
        assert config.enable_backtrace == enable_backtrace
        assert config.diagnose == diagnose
        assert config.sinks == sinks
        assert config.formatters == formatters

    def test_logger_config_level_from_string(self):
        """Test that level accepts string values."""
        # Act
        config = LoggerConfig(level="ERROR")

        # Assert
        assert config.level == "ERROR"

    def test_logger_config_level_from_enum(self):
        """Test that level accepts LogLevel enum values."""
        # Act
        config = LoggerConfig(level=LogLevel.CRITICAL)

        # Assert
        assert config.level == LogLevel.CRITICAL

    def test_logger_config_nested_validation(self):
        """Test that nested sink and formatter configs are validated."""
        # Arrange
        invalid_sink = {"name": ""}  # Empty name should fail

        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            LoggerConfig(sinks=[invalid_sink])  # type: ignore

        assert "String should have at least 1 character" in str(exc_info.value)


class TestModelSerialization:
    """Test model serialization and deserialization."""

    def test_component_metadata_dict_serialization(self):
        """Test ComponentMetadata to/from dict conversion."""
        # Arrange
        metadata = ComponentMetadata(
            name="TestSink",
            version="1.0.0",
            component_type=ComponentType.SINK,
            author="Test Author",
        )

        # Act
        data = metadata.model_dump()
        restored = ComponentMetadata.model_validate(data)

        # Assert
        assert restored == metadata
        assert data["component_type"] == ComponentType.SINK  # Enum preserved in model_dump()

    def test_sink_config_dict_serialization(self):
        """Test SinkConfig to/from dict conversion."""
        # Arrange
        config = SinkConfig(
            name="file_sink",
            level=LogLevel.WARNING,
            format="{time} - {message}",
            options={"path": "/tmp/test.log"},
        )

        # Act
        data = config.model_dump()
        restored = SinkConfig.model_validate(data)

        # Assert
        assert restored == config
        assert data["level"] == 30  # LogLevel.WARNING value

    def test_logger_config_complex_serialization(self):
        """Test LoggerConfig with nested objects serialization."""
        # Arrange
        config = LoggerConfig(
            level=LogLevel.DEBUG,
            sinks=[
                SinkConfig(name="console", level=LogLevel.INFO),
                SinkConfig(name="file", options={"path": "app.log"}),
            ],
            formatters=[
                FormatterConfig(name="plain"),
                FormatterConfig(name="rich", options={"theme": "dark"}),
            ],
        )

        # Act
        data = config.model_dump()
        restored = LoggerConfig.model_validate(data)

        # Assert
        assert restored == config
        assert len(data["sinks"]) == 2
        assert len(data["formatters"]) == 2


class TestModelValidationEdgeCases:
    """Test edge cases and error conditions in model validation."""

    def test_sink_config_with_path_object(self):
        """Test SinkConfig with Path object in options."""
        # Arrange
        path_obj = Path("/tmp/app.log")

        # Act
        config = SinkConfig(name="file_sink", options={"path": path_obj})

        # Assert
        assert config.options["path"] == path_obj

    def test_logger_config_empty_lists(self):
        """Test LoggerConfig with explicitly empty lists."""
        # Act
        config = LoggerConfig(sinks=[], formatters=[])

        # Assert
        assert config.sinks == []
        assert config.formatters == []

    def test_component_metadata_long_description(self):
        """Test ComponentMetadata with very long description."""
        # Arrange
        long_description = "A" * 1000  # Very long description

        # Act
        metadata = ComponentMetadata(
            name="TestSink",
            version="1.0.0",
            component_type=ComponentType.FORMATTER,
            description=long_description,
        )

        # Assert
        assert metadata.description == long_description

    def test_sink_config_complex_options(self):
        """Test SinkConfig with complex nested options."""
        # Arrange
        complex_options = {
            "connection": {
                "host": "localhost",
                "port": 5432,
                "ssl": True,
            },
            "retry": {
                "attempts": 3,
                "delay": 1.5,
            },
            "filters": ["error", "critical"],
        }

        # Act
        config = SinkConfig(name="database_sink", options=complex_options)

        # Assert
        assert config.options == complex_options
