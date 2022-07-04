from entrypoint import entrypoint

from web.main import web

entrypoint(__name__).call(web)
