name: "📚 Documentation Issue"
description: "Report an error, typo, or missing information in the documentation."
title: "[Docs] A brief title for the documentation issue"
labels: ["documentation"]
body:

- type: input
  id: page-url
  attributes:
  label: Page URL
  description: "Please provide the URL of the documentation page with the issue."
  placeholder: "https://stolaslog.readthedocs.io/en/latest/user_guide/quickstart.html"
  validations:
  required: true
- type: textarea
  id: description
  attributes:
  label: Describe the issue
  description: "A clear and concise description of what is wrong or missing. Is it a typo? Is the explanation unclear?
  Is an example not working?"
  validations:
  required: true
