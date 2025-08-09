import os
import sys
from importlib import metadata
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.application import Sphinx

sys.path.insert(0, os.path.abspath("../../src"))

project_metadata: Any = metadata.metadata("stolas-log")

project: str = project_metadata["Name"]
author_string: str = project_metadata.get("Author-Email", "Unknown Author")
author: str = author_string.split("<")[0].strip()
copyright: str = f"2025, {author}"

version: str = metadata.version("stolas-log")
release: str = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_rtd_theme",
    "sphinx_rtd_dark_mode",
    "sphinx_feedback",
]

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"
nitpicky = True

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
default_dark_mode = 1

html_theme_options: dict[str, Any] = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}

html_context: dict[str, Any] = {
    "github_user": "Qu1nel",
    "github_repo": "StolasLog",
    "github_version": "main",
    "display_github": True,
}

feedback_project_id = "Qu1nel/StolasLog"
feedback_issue_template = (
    "**Feedback on page: {{ page.relpath }}**\n\n"
    "**Rating: {{ rating }}**\n\n"
    "**Comment:**\n{{ comment }}\n\n"
    "--- (auto-generated) ---\n"
    "Browser: {{ user.browser }}\n"
    "OS: {{ user.os }}"
)

add_module_names = False
autodoc_member_order = "bysource"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
napoleon_use_rtype = False
napoleon_use_ivar = True
myst_heading_anchors = 3


def setup(app: "Sphinx") -> None:
    app.add_css_file("css/stolaslog.css")
    app.add_js_file("js/copybutton.js")
