"""Helper functions for Ista API."""
import json
import logging
from typing import Any, Dict

import requests

logger = logging.getLogger(__name__)

API_BASE_URL = "https://www.ista-webconso.fr/"
API_TIMEOUT = 10


class Helpers:
    """Helper functions for Ista API."""

    @staticmethod
    def call_api(
        url_path: str,
        method: str,
        json_object: Dict[Any, Any] | None = None,
        headers: Dict[Any, Any] | None = None,
    ) -> tuple:
        """Make API calls by passing endpoint, header and body."""
        response = None
        status_code = None

        try:
            logger.debug("=======call_api=============================")
            logger.debug("[%s] calling '%s' api", method, url_path)
            logger.debug("API call URL: \n  %s%s", API_BASE_URL, url_path)
            logger.debug("API call headers: \n  %s", json.dumps(headers))
            logger.debug("API call json: \n  %s", json.dumps(json_object))
            if method.lower() == "get":
                req = requests.get(
                    API_BASE_URL + url_path,
                    json=json_object,
                    headers=headers,
                    timeout=API_TIMEOUT,
                )
            elif method.lower() == "post":
                req = requests.post(
                    API_BASE_URL + url_path,
                    json=json_object,
                    headers=headers,
                    timeout=API_TIMEOUT,
                )
            elif method.lower() == "put":
                req = requests.put(
                    API_BASE_URL + url_path,
                    json=json_object,
                    headers=headers,
                    timeout=API_TIMEOUT,
                )
        except requests.exceptions.RequestException as err:
            logger.debug(err)
        except Exception as err:  # pylint: disable=broad-except
            logger.debug(err)
        else:
            if req.status_code == 200:
                status_code = 200
                if req.content:
                    response = req.json()
                    logger.debug("API response: \n\n  %s \n ", response)
            else:
                logger.debug("Unable to fetch %s%s", API_BASE_URL, url_path)
        return response, status_code

if __name__ == "__main__":
    pass