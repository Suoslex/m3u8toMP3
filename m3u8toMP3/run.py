import os
import sys
import asyncio
from pathlib import Path
from argparse import ArgumentParser, Namespace

from m3u8toMP3.file_helper import FileHelper
from m3u8toMP3.converter import M3u8Converter
from m3u8toMP3.utils import get_application_path


async def convert_m3u8_to_mp3(path_to_m3u8: str, output_path: str = None):
    """
    Converts a M3U8 file located in given path to MP3.

    Parameters
    ----------
    path_to_m3u8: str
        URL or local path to a file where M3U8 file is located.

    output_path: str
        Local path to output MP3 file, where it is saved.
    """
    m3u8_bytes = await FileHelper.get_file_bytes(path_to_m3u8)
    mp3_bytes = await M3u8Converter.convert_to_mp3(m3u8_bytes)
    if not output_path:
        m3u8_path = Path(path_to_m3u8)
        if FileHelper.check_if_local_path(path_to_m3u8):
            output_path = m3u8_path.parent / f"{m3u8_path.stem}.mp3"
        else:
            output_path = get_application_path() / f"{m3u8_path.stem}.mp3"
    with open(output_path, 'wb') as output_file:
        output_file.write(mp3_bytes)


def parse_cmd_args() -> Namespace:
    parser = ArgumentParser(description="M3U8 audio stream to MP3 converter.")
    parser.add_argument(
        "m3u8_path",
        help="Path to M3U8 file. Can be both a URL and a local path."
    )
    parser.add_argument(
        "output_path",
        nargs='?',
        help="Local path to save output MP3 file."
    )
    return parser.parse_args()


def _exception_handler(
        exception_type,
        exception,
        traceback,
        debug_hook=sys.excepthook
):
    if os.getenv('DEBUG', None):
        debug_hook(exception_type, exception, traceback)
    else:
        print(f"ERROR: {exception}")


async def main():
    sys.excepthook = _exception_handler
    cmd_args = parse_cmd_args()
    return await convert_m3u8_to_mp3(cmd_args.m3u8_path, cmd_args.output_path)


if __name__ == "__main__":
    asyncio.run(main())
