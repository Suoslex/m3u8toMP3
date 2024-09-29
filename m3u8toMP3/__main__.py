import os
import sys
import asyncio
from argparse import ArgumentParser, Namespace

from m3u8toMP3.run import convert_m3u8_to_mp3


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

