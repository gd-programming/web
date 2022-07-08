from aiohttp.web import HTTPFound, Request, Response

from web.constants import DOMAIN, EMAIL, EMAIL_TO
from web.core import routes
from web.utils import identifier

NAME = "name"
EMAIL_ROUTE = f"/email/{identifier(NAME)}"


@routes.get(EMAIL_ROUTE)
def handle_docs(request: Request) -> Response:
    name = request.match_info[NAME]

    raise HTTPFound(EMAIL_TO + EMAIL.format(name, DOMAIN))
