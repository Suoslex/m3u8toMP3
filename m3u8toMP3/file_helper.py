from pathlib import Path
from urllib.parse import urlparse

from m3u8toMP3.utils import get_response
from m3u8toMP3.exceptions import FileBytesRetrievalError


class FileHelper:
    @classmethod
    async def get_file_bytes(cls, path: str) -> bytes:
        """
        Retrieves file bytes from the given path.
        The path can be both a local path or a URL.

        Parameters
        ----------
        path: str
            Path to the file to retrieve bytes from.
            Can be both a local path or a URL.

        Returns
        -------
        bytes
            The content of the file by the given path.
        """
        if cls.check_if_url(path):
            return await cls.get_file_bytes_from_url(path)
        if cls.check_if_local_path(path):
            return await cls.get_file_bytes_from_local_path(path)
        raise FileBytesRetrievalError(f"Invalid file path passed: {path}.")

    @classmethod
    async def get_file_bytes_from_url(cls, url: str) -> bytes:
        """
        Retrieve file bytes from the given URL.

        Parameters
        ----------
        url: str
            URL to a file to get bytes from.

        Returns
        -------
        bytes
            Contents of the file located on given URL.
        """
        return await get_response(url)

    @classmethod
    async def get_file_bytes_from_local_path(cls, path: str):
        """
         Retrieve file bytes from the given local path.

         Parameters
         ----------
         path: str
             Local path to a file to get bytes from.

         Returns
         -------
         bytes
             Contents of the file located in given local path.
         """
        with open(path, 'rb') as file:
            return file.read()

    @classmethod
    def check_if_url(cls, string: str) -> bool:
        """
        Checks if the passed string is a URL or not.

        Parameters
        ----------
        string: str
            String to make a check.

        Returns
        -------
        bool
            True, if the passed string is a URL, and False otherwise.
        """
        url = urlparse(string)
        return all([url.scheme, url.netloc])

    @classmethod
    def check_if_local_path(cls, string: str) -> bool:
        """
        Checks if the passed string is a local path to a file or not.

        Parameters
        ----------
        string: str
            String to check.

        Returns
        -------
        bool
            True, if the passed string is a local path, and False otherwise.
        """
        return Path(string).exists()
