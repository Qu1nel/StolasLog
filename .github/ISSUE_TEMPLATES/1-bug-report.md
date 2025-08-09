name: "🐞 Bug Report"
description: "Report an issue to help us improve StolasLog."
title: "[Bug] A brief, descriptive title"
labels: ["bug"]
body:

- type: markdown
  attributes:
  value: |
  Thank you for taking the time to fill out this bug report!
  Please be as detailed as possible.

- type: textarea
  id: description
  attributes:
  label: Describe the bug
  description: A clear and concise description of what the bug is.
  placeholder: "When I call logger.setup() with rotation='1 day', it creates a new file every second..."
  validations:
  required: true

- type: textarea
  id: reproduction
  attributes:
  label: To Reproduce
  description: Please provide a minimal, self-contained code snippet that reproduces the behavior.
  placeholder: |
  ```python
  from stolas_log import logger

      # 1. Configuration
      logger.setup(...)

      # 2. Code that causes the bug
      logger.info("This should go to a daily file.")

      # 3. What happens
      # => Creates multiple files instead of one.
      ```
  validations:
  required: true

- type: textarea
  id: expected
  attributes:
  label: Expected Behavior
  description: A clear and concise description of what you expected to happen.
  placeholder: "I expected only one log file to be created for the entire day."
  validations:
  required: true

- type: input
  id: version
  attributes:
  label: StolasLog Version
  description: "What version of `stolas-log` are you using? (e.g., 0.1.0)"
  validations:
  required: true

- type: dropdown
  id: os
  attributes:
  label: Operating System
  multiple: true
  options:
    - Windows
    - macOS
    - Linux
    - WSL
      validations:
      required: true

- type: textarea
  id: context
  attributes:
  label: Additional Context
  description: Add any other context about the problem here (screenshots, logs, etc.).
