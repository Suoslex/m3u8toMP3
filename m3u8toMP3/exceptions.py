class M3U8toMP3Error(Exception):
    message = "There was an error executing the script"

    def __init__(self, detail: str = None):
        message = self.message
        message += f": {detail}" if detail else "."
        super().__init__(f"{message}")


class RequestError(M3U8toMP3Error, RuntimeError):
    message = "There was an error getting a response from the URL"


class FileBytesRetrievalError(M3U8toMP3Error, FileNotFoundError):
    message = "There was an error trying to retrieve bytes from the file"
