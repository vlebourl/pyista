"""Ista Webconsole API."""

import logging

from pyista.helpers import Helpers

_LOGGER = logging.getLogger(__name__)


class Ista:
    """Ista main class."""

    def __init__(self) -> None:
        """Initialize Ista class."""
        self._base_header = Helpers.req_headers()
        _LOGGER.debug("Ista class initialized")
