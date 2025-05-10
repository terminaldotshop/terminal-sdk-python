from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `terminal_shop.resources` module.

    This is used so that we can lazily import `terminal_shop.resources` only when
    needed *and* so that users can just import `terminal_shop` and reference `terminal_shop.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("terminal_shop.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
