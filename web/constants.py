from pathlib import Path

ROOT = Path(__file__).parent

ROOT_ROUTE = "/"

TEXT_HTML = "text/html"
TEXT_PLAIN = "text/plain"

BASE_NAME = "base.html"
HOME_NAME = "home.html"

CSS_NAME = "css"
STATIC_NAME = "static"
TEMPLATES_NAME = "templates"

STATIC = ROOT / STATIC_NAME
CSS = STATIC / CSS_NAME
TEMPLATES = ROOT / TEMPLATES_NAME

DEFAULT_INPUT_NAME = "input.css"
DEFAULT_OUTPUT_NAME = "output.css"

DEFAULT_INPUT = CSS / DEFAULT_INPUT_NAME
DEFAULT_OUTPUT = CSS / DEFAULT_OUTPUT_NAME

EMAIL_TO = "mailto:"
DOMAIN = "gd-programming.org"

EMAIL = "{}@{}"

DISCORD_NAME = "discord"

DISCORD_LINK = "https://discord.gg/jEwtDBK"

GITHUB_NAME = "github"

GITHUB_LINK = "https://github.com/gd-programming"

NAME_TO_LINK = {
    DISCORD_NAME: DISCORD_LINK,
    GITHUB_NAME: GITHUB_LINK,
}

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 6942

DEFAULT_NAME = "web"
