from pathlib import Path

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

