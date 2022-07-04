from aiohttp.web import HTTPFound, Request, Response

from web.constants import NAME_TO_LINK, ROOT_ROUTE
from web.core import routes
from web.typing import Handler


def create_redirect(name: str, link: str) -> Handler:
    @routes.get(ROOT_ROUTE + name)
    async def handle_redirect(request: Request) -> Response:
        raise HTTPFound(link)

    return handle_redirect


for name, link in NAME_TO_LINK.items():
    create_redirect(name, link)
