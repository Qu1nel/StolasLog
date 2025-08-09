# ==============================================================================
#  Makefile for the StolasLog Project
#  - Author: Qu1nel
#  - Version: 1.0 (Full Dev Environment & Release Automation)
# ==============================================================================

# --- Color Codes for Output ---
RESET   = \033[0m
BOLD    = \033[1m
RED     = \033[31m
GREEN   = \033[32m
YELLOW  = \033[33m
CYAN    = \033[36m

# --- Variables ---
PYTHON_VERSION  := 3.11
UV_RUN          := uv run
RUFF            := $(UV_RUN) ruff
PYTEST          := $(UV_RUN) pytest
MYPY            := $(UV_RUN) mypy
BUILD           := $(UV_RUN) build
TWINE           := $(UV_RUN) twine
COMMITIZEN      := $(UV_RUN) cz
TOX             := $(UV_RUN) tox
SEM_RELEASE     := $(UV_RUN) semantic-release

.DEFAULT_GOAL := help
.PHONY: setup sync lint format check mypy test coverage coverage-html security docs build commit changelog version release publish-test publish full-clean clean help

# ==============================================================================
#  PROJECT SETUP & DEPENDENCY MANAGEMENT
# ==============================================================================
setup: ## Install all dependencies for development into a new venv.
	@echo "$(CYAN)› Creating virtual environment with Python $(PYTHON_VERSION)...$(RESET)"
	@uv venv -p $(PYTHON_VERSION) --seed
	@echo "$(CYAN)› Installing all project dependencies (including dev, docs, performance)...$(RESET)"
	@uv pip install -e ".[dev,docs,performance]"
	@echo "$(GREEN)✅ Setup complete. Activate with 'source .venv/bin/activate'.$(RESET)"
	@make clean

sync: ## Synchronize the venv with pyproject.toml.
	@echo "$(CYAN)› Syncing virtual environment with pyproject.toml...$(RESET)"
	@uv pip install -e ".[dev,docs,performance]"
	@echo "$(GREEN)✅ Dependencies are up to date.$(RESET)"

# ==============================================================================
#  LINTING & STATIC ANALYSIS
# ==============================================================================
lint: format check mypy ## Run all formatters, linters, and type checkers.
	@echo "$(GREEN)✅ All checks passed successfully!$(RESET)"

format: ## Auto-format code with ruff.
	@echo "$(CYAN)› Formatting code with ruff...$(RESET)"
	@$(RUFF) format src/ tests/

check: ## Check for linting errors with ruff (with auto-fix).
	@echo "$(CYAN)› Checking for linting errors with ruff...$(RESET)"
	@$(RUFF) check src/ tests/ --fix

mypy: ## Run static type checking with mypy.
	@echo "$(CYAN)› Running static type checking with mypy...$(RESET)"
	@$(MYPY) src/stolas_log/

# ==============================================================================
#  TESTING & SECURITY
# ==============================================================================
tox: ## Run the full tox suite for multi-version local testing.
	@echo "$(CYAN)› Running the full tox test suite...$(RESET)"
	@$(TOX)

test: ## Run the test suite with pytest.
	@echo "$(CYAN)› Running tests with pytest...$(RESET)"
	@$(PYTEST) tests/

coverage: ## Run tests and show a coverage report in the console.
	@echo "$(CYAN)› Running tests with coverage...$(RESET)"
	@$(PYTEST) --cov=src/stolas_log --cov-report=term-missing tests/

coverage-html: ## Run tests and generate an HTML coverage report.
	@echo "$(CYAN)› Running tests and generating HTML coverage report...$(RESET)"
	@$(PYTEST) --cov=src/stolas_log --cov-report=html tests/
	@echo "$(GREEN)✅ HTML report generated in 'htmlcov/'.$(RESET)"

security: ## Scan for known security vulnerabilities in dependencies.
	@echo "$(CYAN)› Scanning for security vulnerabilities...$(RESET)"
	@uv pip audit

# ==============================================================================
#  DOCUMENTATION
# ==============================================================================
docs: ## Build the documentation using Sphinx.
	@echo "$(CYAN)› Building documentation...$(RESET)"
	@$(UV_RUN) sphinx-build docs/source docs/build/html -b html
	@echo "$(GREEN)✅ Documentation built in 'docs/build/html/'.$(RESET)"

docs-live: ## Build, watch for changes, and serve docs with live-reload.
	@echo "$(CYAN)› Starting live-reloading documentation server at http://127.0.0.1:8000/...$(RESET)"
	@$(UV_RUN) sphinx-autobuild docs/source docs/build/html --open-browser

# ==============================================================================
#  COMMIT & RELEASE AUTOMATION
# ==============================================================================
commit: ## Interactively create a conventional commit with Commitizen.
	@echo "$(CYAN)› Starting interactive commit session...$(RESET)"
	@$(COMMITIZEN) commit

changelog: ## (Dry Run) Preview the auto-generated changelog.
	@echo "$(CYAN)› Generating changelog from conventional commits...$(RESET)"
	@$(SEM_RELEASE) changelog
	@echo "$(YELLOW)Note: This is a dry run. No files were changed.$(RESET)"

version: ## (Dry Run) Preview the new version and changelog.
	@echo "$(CYAN)› Bumping version and generating changelog...$(RESET)"
	@$(SEM_RELEASE) version --dry-run
	@echo "$(YELLOW)Note: This is a dry run. No files were changed, no tags created.$(RESET)"

release: ## Create a new version, update changelog, commit, and tag locally.
	@echo "$(YELLOW)› Starting local release process...$(RESET)"
	@$(SEM_RELEASE) version
	@echo "$(GREEN)✅ Local release complete! Review changes, then run 'git push && git push --tags'.$(RESET)"

# ==============================================================================
#  MANUAL PUBLISHING
# ==============================================================================
build: ## Build the package into wheel and sdist artifacts.
	@echo "$(CYAN)› Building package...$(RESET)"
	@$(BUILD)
	@echo "$(GREEN)✅ Package built in 'dist/'.$(RESET)"

publish: build ## (Manual) Publish package to the official PyPI repository.
	@echo "$(RED)$(BOLD)› Uploading package to the REAL PyPI...$(RESET)"
	@$(TWINE) upload dist/*

# ==============================================================================
#  CLEANUP
# ==============================================================================
full-clean: ## Remove venv, cache files, and build artifacts.
	@echo "$(RED)› Performing full clean, including virtual environment...$(RESET)"
	@rm -rf .venv
	@$(MAKE) clean
	@echo "$(GREEN)✅ Full cleanup complete.$(RESET)"

clean: ## Remove cache files and build artifacts.
	@echo "$(YELLOW)› Cleaning up cache and build artifacts...$(RESET)"
	@python -c "import shutil, glob; [shutil.rmtree(p, ignore_errors=True) for p in ['.tox', '.ruff_cache', '.pytest_cache', '.mypy_cache', 'htmlcov', '.coverage', 'dist', 'build'] + glob.glob('src/*.egg-info') + glob.glob('**/__pycache__')]"
	@pre-commit clean
	@echo "$(GREEN)✅ Cleanup complete.$(RESET)"

# ==============================================================================
#  HELP
# ==============================================================================
help: ## Show this help message.
	@echo ""
	@echo "  $(BOLD)StolasLog - Makefile Help$(RESET)"
	@echo "  ---------------------------"
	@echo "  Usage: $(GREEN)make$(RESET) $(CYAN)<target>$(RESET)"
	@echo ""
	@echo "  $(YELLOW)Available targets:$(RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "    $(GREEN)%-20s$(RESET) %s\n", $$1, $$2}'