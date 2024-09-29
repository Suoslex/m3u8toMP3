import os
import binascii
from io import BytesIO

import m3u8
from ffmpeg.asyncio import FFmpeg
from Crypto.Cipher import AES

from m3u8toMP3.utils import get_response


class M3u8Converter:
    @classmethod
    async def convert_to_mp3(cls, m3u8_bytes: bytes | BytesIO) -> bytes:
        """
        Converts a m3u8 file to MP3.

        Parameters
        ----------
        m3u8_bytes: bytes | BytesIO
            Content of m3u8 file.

        Returns
        -------
        bytes
            Contents of the MP3 file.
        """
        await cls.check_environment()
        if isinstance(m3u8_bytes, BytesIO):
            m3u8_bytes = m3u8_bytes.read()

        m3u8_obj = m3u8.loads(m3u8_bytes.decode('utf8'))
        media_sequence = m3u8_obj.media_sequence
        host_url = cls._get_host_url(m3u8_obj)
        if host_url is None:
            raise TypeError("Couldn't retrieve host url from m3u8 file.")

        key, raw_mp3 = None, b""
        for i, segment in enumerate(m3u8_obj.segments):
            decrypt_func = lambda x: x
            if segment.key.method == "AES-128":
                if not key:
                    key_uri = segment.key.uri
                    key = await get_response(key_uri)
                ind = i + media_sequence
                iv = binascii.a2b_hex('%032x' % ind)
                cipher = AES.new(key, AES.MODE_CBC, iv=iv)
                decrypt_func = cipher.decrypt

            ts_url = os.path.join(host_url, segment.uri)
            data = await get_response(ts_url)
            raw_mp3 += decrypt_func(data)

        ffmpeg = (
            FFmpeg()
            .option("y")
            .input("pipe:0")
            .output(
                "pipe:1",
                f="mp3",
                ab="320k"
            )
        )
        return await ffmpeg.execute(raw_mp3)

    @staticmethod
    async def check_environment():
        try:
            await FFmpeg().option('h').execute()
        except FileNotFoundError:
            raise EnvironmentError(
                "Please make sure that ffmpeg is installed "
                "and can be executed (ffmpeg -h)."
            )

    @staticmethod
    def _get_host_url(m3u8_obj: m3u8.M3U8):
        media_sequence = m3u8_obj.media_sequence or len(m3u8_obj.keys)
        result = ""
        for i in range(media_sequence):
            try:
                key_uri = m3u8_obj.keys[i].uri
                result = "/".join(key_uri.split("/")[:-1])
                return result
            except AttributeError:
                continue
        return result

