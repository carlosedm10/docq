"""REST API route handlers.

Route handlers can be split across modules files.
Make sure to import the module at the entry point of the Streamlit app.
For Docq that's the `web/index.py`

See Tornado docs for details on the RequestHandler class:
https://www.tornadoweb.org/en/stable/web.html


Naming convention:
module name: route replace `/` with `_`. Example:  `/api/hello/world` -> `hello_world_handler`
class name: route replace capitalise route segments remove `/` and `_`. Example: `/api/hello/world` -> `HelloWorldHandler`
"""

# for now we'll manually add imports. TODO: convert to walk the directory and dynamically import using importlib

from . import (
    chat_completion_handler,  # noqa: F401 DO NOT REMOVE
    hello_handler,  # noqa: F401 DO NOT REMOVE
    rag_completion_handler,  # noqa: F401 DO NOT REMOVE
    spaces_files_handler,  # noqa: F401 DO NOT REMOVE
    spaces_handler,  # noqa: F401 DO NOT REMOVE
    threads_handler,  # noqa: F401 DO NOT REMOVE
    token_handler,  # noqa: F401 DO NOT REMOVE
)
import logging

# Slack integration is optional; only import if available/configured
try:  # noqa: SIM105
    from .integration.slack import index_handler  # noqa: F401 DO NOT REMOVE
    _slack_available = True
except Exception as e:  # broad to avoid hard-failing when slack deps/env missing
    logging.warning("Slack integration not available: %s", e)
    _slack_available = False

__all__ = [
    "chat_completion_handler",
    "hello_handler",
    "rag_completion_handler",
    "spaces_handler",
    "spaces_files_handler",
    "threads_handler",
    "token_handler",
]

if _slack_available:
    __all__.append("index_handler")


def setup() -> None:
    """Fake method to keep the linter happy."""
    pass
