"""Ista Webconsole API."""

import logging

from pyista.helpers import Helpers

_LOGGER = logging.getLogger(__name__)


class Ista:
    """Ista main class."""

    def __init__(self) -> None:
        """Initialize Ista class."""
        _LOGGER.debug("Ista class initialized")
