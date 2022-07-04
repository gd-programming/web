from typing import TypeVar

from aiohttp.web import Application, RouteTableDef, run_app
from jinja2 import Environment, FileSystemLoader

from web.constants import ROOT_ROUTE, STATIC, STATIC_NAME, TEMPLATES

__all__ = ("environment", "routes", "run_app", "setup_app")

environment = Environment(
    loader=FileSystemLoader(TEMPLATES),
    trim_blocks=True,
    lstrip_blocks=True,
    enable_async=True,
)

routes = RouteTableDef()

routes.static(ROOT_ROUTE + STATIC_NAME, STATIC)


A = TypeVar("A", bound=Application)


def setup_app(app: A) -> A:
    app.add_routes(routes)

    return app
