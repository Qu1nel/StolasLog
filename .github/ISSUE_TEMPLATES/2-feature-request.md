name: "🚀 Feature Request"
description: "Suggest a new feature or an enhancement for an existing one."
title: "[Feature] A brief title for your idea"
labels: ["feature request", "enhancement"]
body:

- type: markdown
  attributes:
  value: "Thank you for suggesting an idea! We love hearing from our community."

- type: textarea
  id: problem-description
  attributes:
  label: Is your feature request related to a problem? Please describe.
  description: "A clear and concise description of what the problem is. Ex. I'm always frustrated when..."
  placeholder: "It's currently difficult to create a log sink that sends messages to Telegram because..."
  validations:
  required: true

- type: textarea
  id: solution-description
  attributes:
  label: Describe the solution you'd like
  description: "A clear and concise description of what you want to happen. How would the API look? Provide code
  examples if you can."
  placeholder: |
  "I would like a new `TelegramSink` that I can configure like this:
  ```python
  logger.setup(sinks=[TelegramSink(api_key='...', chat_id='...')])
  ```
  It should automatically handle rate limits."

- type: textarea
  id: alternatives
  attributes:
  label: Describe alternatives you've considered
  description: "A clear and concise description of any alternative solutions or features you've considered."

- type: checkboxes
  id: checklist
  attributes:
  label: "Checklist"
  description: "Before you submit, please make sure you've done the following."
  options:
  - label: I have searched the existing [issues](https://github.com/Qu1nel/StolasLog/issues) and have not found a
  similar feature request.
  required: true
