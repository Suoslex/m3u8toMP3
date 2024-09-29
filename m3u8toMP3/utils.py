import sys
from pathlib import Path

import httpx

from m3u8toMP3.exceptions import RequestError


async def get_response(url: str) -> bytes:
    """
    Retrieves contents of the GET response on the passed URL.

    Parameters
    ----------
    url: str
        Address to get response from.

    Returns
    -------
    bytes
        Contents of the response

    Raises
    ----------
    m3u8toMP3.exceptions.RequestError
        If the request was successfully sent and a response retrieved, but
        the response status code is different from 200.
    httpx.RequestError
        Other request errors
    """
    async with httpx.AsyncClient() as client:
        data_response = await client.get(url)
        if data_response.status_code != 200:
            raise RequestError(
                f"Got {data_response.status_code} status code sending "
                f"a request to {url} instead of 200."
            )
        result = data_response.content
    return result


def get_application_path() -> Path:
    """
    Get the current application path (where is the program executed).

    Returns
    -------
    str
        Directory of the application path.
    """
    if getattr(sys, 'frozen', False):
        application_path = Path(sys.executable).parent
    else:
        application_path = Path(__file__).parent
    return application_path
