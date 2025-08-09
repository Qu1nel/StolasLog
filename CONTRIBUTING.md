# Contributing to StolasLog 🦉

First and foremost, thank you for considering contributing to StolasLog! We welcome any and all contributions, from
fixing a typo in the documentation to implementing a brand new, powerful sink.

This document provides guidelines to ensure that contributing is a smooth and effective process for everyone involved.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements or New Features](#suggesting-enhancements-or-new-features)
    - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Our Workflow: Commits, Style, and Testing](#our-workflow-commits-style-and-testing)
    - [Git Commit Messages: The Most Important Rule](#git-commit-messages-the-most-important-rule)
    - [Python Styleguide](#python-styleguide)
    - [Static Type Checking](#static-type-checking)
    - [Testing](#testing)

## Code of Conduct

By participating in this project, you are expected to uphold our [Code of Conduct](./.github/CODE_OF_CONDUCT.md). Please
read it
before you start. We are committed to fostering an open and welcoming environment.

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please ensure it hasn't already been reported by searching through
the [GitHub Issues](https://github.com/Qu1nel/StolasLog/issues). If you're unable to find an open issue addressing the
problem, please [open a new one](https://github.com/Qu1nel/StolasLog/issues/new?template=bug_report.md) using the "Bug
Report" template.

### Suggesting Enhancements or New Features

We are always open to new ideas! If you have a suggestion for an enhancement or a new feature, please open a new issue
using the "Feature Request" template:

- [**Feature Request**](https://github.com/Qu1nel/StolasLog/issues/new?template=feature_request.md)

### Submitting Pull Requests

If you have code to contribute, please submit it as a Pull Request (PR).

1. Fork the repository and create your branch from `main`.
2. Set up your local development environment (see [Development Setup](#development-setup)).
3. Make your changes, following our styleguides (see below).
4. Add tests for your changes.
5. Ensure all checks pass by running `make lint` and `make test`.
6. Update the documentation if your changes require it.
7. Open a new Pull Request, filling out the provided template.

## Development Setup

We use `uv` and `make` to provide a simple and consistent development experience.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Qu1nel/StolasLog.git
   cd StolasLog
   ```
2. **Run the setup command:**
   ```bash
   make setup
   ```
   This command will create a virtual environment in `.venv/` and install all necessary dependencies for development.

3. **Activate the virtual environment:**
    * On Linux/macOS/WSL: `source .venv/bin/activate`
    * On Windows: `.venv\Scripts\activate`

Now you are ready to start coding!

## Our Workflow: Commits, Style, and Testing

We use a suite of tools to maintain high code quality and automate our release process. These are automatically enforced
by our pre-commit hooks, so please install them with `pre-commit install`.

### Git Commit Messages: The Most Important Rule

Our project uses **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)**. This is not just a
suggestion, it's a **strict requirement** because our release and changelog generation depends on it.

The easiest way to create a compliant commit message is to use our interactive helper:

```bash
make commit
```

This will launch `commitizen` and guide you through the process of creating a perfect commit message.

### Python Styleguide

Our codebase is automatically formatted and linted using **Ruff**. Before committing, please run:

```bash
make lint
```

This command will format your code (`ruff format`), check for any style violations (`ruff check`), and run the type
checker (`mypy`).

### Static Type Checking

We use **Mypy** in strict mode. All new code must be fully type-hinted and pass `mypy` checks. You can run the type
checker independently with:

```bash
make mypy
```

### Testing

This project maintains a high standard of test coverage.

- **Run the full test suite:**
  ```bash
  make test
  ```
- **Run tests with a coverage report:**
  ```bash
  make coverage
  ```
- **Generate an interactive HTML coverage report:**
  ```bash
  make coverage-html
  ```

All new features and bug fixes **must** be accompanied by corresponding tests to be accepted.

---

Thank you again for your interest in contributing! We look forward to your ideas.
