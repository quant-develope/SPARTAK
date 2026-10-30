"""All Greek pages."""
import el_main
import el_build
import el_more
import el_areas
from el_more import not_found  # noqa: F401


def pages():
    return el_main.pages() + el_build.pages() + el_more.pages() + el_areas.pages()
