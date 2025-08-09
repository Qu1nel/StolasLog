from typing import Any

from commitizen.cz.conventional_commits import ConventionalCommitsCz


class StolasCz(ConventionalCommitsCz):  # type: ignore[misc]
    def questions(self) -> list[dict[str, Any]]:
        return [
            {
                "type": "list",
                "name": "change_type",
                "message": "Select the type of change you are committing",
                "choices": [
                    {"value": "feat", "name": "feat:     A new feature. (MINOR)"},
                    {"value": "fix", "name": "fix:      A bug fix. (PATCH)"},
                    {"value": "perf", "name": "perf:     A code change that improves performance. (PATCH)"},
                    {"value": "revert", "name": "revert:   Reverts a previous commit. (PATCH)"},
                    {"value": "docs", "name": "docs:     Documentation only changes."},
                    {"value": "style", "name": "style:    Changes that do not affect the meaning of the code."},
                    {
                        "value": "refactor",
                        "name": "refactor: A code change that neither fixes a bug nor adds a feature.",
                    },
                    {"value": "test", "name": "test:     Adding missing or correcting existing tests."},
                    {
                        "value": "build",
                        "name": "build:    Changes that affect the build system or external dependencies.",
                    },
                    {"value": "ci", "name": "ci:       Changes to CI configuration files and scripts."},
                    {"value": "chore", "name": "chore:    Other changes that don't modify src or test files."},
                ],
            },
            {
                "type": "input",
                "name": "change_scope",
                "message": "What is the scope of this change (e.g., 'config', 'sinks')? (press Enter to skip)\n",
            },
            {
                "type": "input",
                "name": "summary",
                "message": "Write a short, imperative tense description of the change.\n",
            },
            {
                "type": "input",
                "name": "body",
                "message": "Provide a longer description of the change. (press Enter to skip)\n",
            },
            {
                "type": "confirm",
                "name": "is_breaking",
                "message": "Are there any BREAKING CHANGES?",
                "default": False,
            },
            {
                "type": "input",
                "name": "breaking_change",
                "message": "Describe the breaking changes.\n",
                "when": lambda answers: answers.get("is_breaking", False),
            },
            {
                "type": "input",
                "name": "issues",
                "message": "List any issues closed by this change (e.g., 'Closes #123'). (press Enter to skip)\n",
            },
        ]

    def message(self, answers: dict[str, str]) -> str:
        change_type = answers.get("change_type", "")
        scope = f"({answers.get('change_scope')})" if answers.get("change_scope") else ""
        breaking = "!" if answers.get("is_breaking") else ""
        summary = answers.get("summary", "")
        body = f"\n\n{answers.get('body')}" if answers.get("body") else ""
        breaking_change = (
            f"\n\nBREAKING CHANGE: {answers.get('breaking_change')}" if answers.get("breaking_change") else ""
        )
        issues = f"\n\n{answers.get('issues')}" if answers.get("issues") else ""

        return f"{change_type}{scope}{breaking}: {summary}{body}{breaking_change}{issues}"

    def bump_map(self) -> dict[str, str]:
        parent_map: dict[str, str] = super().bump_map()
        parent_map["revert"] = "PATCH"
        return parent_map

    def change_type_map(self) -> dict[str, str]:
        parent_map: dict[str, str] = super().change_type_map()
        parent_map.update(
            {
                "revert": "Reverts",
            }
        )
        return parent_map

    def info(self) -> str:
        return """
StolasLog Commitizen Rules (Conventional Commits)
--------------------------------------------------

This tool helps create standardized commit messages for the StolasLog project.
Following this format is crucial for automated versioning and changelog generation.

*STRUCTURE:*
  <type>(<scope>)!: <summary>
  <-- BLANK LINE -->
  [optional body]
  <-- BLANK LINE -->
  [optional footer(s)]

*COMMIT TYPES:*
  - feat:     A new feature for the user (bumps MINOR version).
  - fix:      A bug fix for the user (bumps PATCH version).
  - perf:     A code change that improves performance (bumps PATCH version).
  - revert:   Reverts a previous commit (bumps PATCH version).
  - docs:     Changes to documentation.
  - style:    Code style changes (formatting, etc).
  - refactor: Code changes that neither fix a bug nor add a feature.
  - test:     Adding or correcting tests.
  - build:    Changes to the build system or dependencies.
  - ci:       Changes to CI/CD configuration.
  - chore:    Routine tasks, maintenance (e.g., project setup).

*EXAMPLES:*
  - Simple fix:
    fix(config): resolve issue with rotation size parsing

  - New feature with scope:
    feat(sinks): add new async Telegram sink

  - Breaking change:
    refactor(core)!: change setup_logger API to use sink objects

    BREAKING CHANGE: The `setup_logger` function no longer accepts simple kwargs like `log_file_path`. All sinks must now be configured via a list of Sink objects.

  - Revert commit:
    revert: feat(sinks): add new async Telegram sink

    This reverts commit a1b2c3d4.

  - Chore for initial setup:
    chore(project): initial project setup and configuration

See https://www.conventionalcommits.org/ for full specification.
"""
