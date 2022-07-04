"""..."""

__description__ = "..."
__url__ = "https://github.com/gd-programming/web"

__title__ = "web"
__author__ = "GD Programming"
__license__ = "MIT"
__version__ = "0.1.0"

from web import modules
from web.core import setup_app
from web.main import create_and_run_app

__all__ = ("modules", "create_and_run_app", "setup_app")
