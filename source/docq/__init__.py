"""Docq module."""
import importlib.metadata as _md

if __package__ is None:
    raise ValueError("Package name is not defined")

m = _md.metadata(__package__)

def _first_available(*keys: str, default: str | None = None) -> str | None:
    for k in keys:
        v = m.get(k)
        if v:
            return v
    return default

# Project URLs come as repeated "Project-URL" headers
project_urls_list = m.get_all("Project-URL") or []
project_urls: dict[str, str] = {}
for item in project_urls_list:
    try:
        key, value = item.split(", ", 1)
        project_urls[key] = value
    except ValueError:
        continue

__version__ = _first_available("Version", default="0.0.0")
__version_str__ = str(__version__)
__summary__ = _first_available("Summary", default="")
__description__ = _first_available("Description", default="")

# Different build backends name this field differently
__homepage_url__ = _first_available("Home-page", "Homepage", "home_page", "home-page", default="https://docq.ai")
__documentation_url__ = project_urls.get("Documentation", "https://docqai.github.io/docq")
__repository_url__ = project_urls.get("Repository", "https://github.com/docqai/docq")
__author_email__ = _first_available("Author-email", default="")
__maintainer_email__ = _first_available("Maintainer-email", default="")