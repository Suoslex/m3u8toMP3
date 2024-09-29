# m3u8toMP3 

Based on **asvatov/m3u82mp3** simple module, the program converts m3u8 
audio streams to MP3 files.

Key features:

- Asynchronous (asyncio)
- Can be used both with terminal (bash, cmd) and inside your python scripts.
- Can work with URLs, local paths to your M3U8 files and with
  raw bytes objects inside your scripts.
- ffmpeg tends to cut the beginning and the ending of 
  streams when converting to MP3, the script fixes this issue.

## Dependencies

The script requires **ffmpeg** to be installed on your system.

You can install it using following commands:

MacOS:
```shell
brew install ffmpeg
```
Debian/Ubuntu:
```shell
apt update && apt upgrade
apt install ffmpeg
```
For Windows and other OS, please refer to the according tutorial 
on the internet.

To make sure the ffmpeg was installed properly, 
execute the following command in your terminal:
```shell
ffmpeg -h
```
If you get any errors ("command not found: ffmpeg", for example) 
then something went wrong during ffmpeg installation.
Please try reinstalling or find help on the Internet.


## Installation and usage as an executable

Download the latest release from the 
[Releases](https://github.com/Suoslex/m3u8toMP3/releases) page.
For example:

```shell
curl -L https://github.com/Suoslex/m3u8toMP3/releases/download/0.1.1/m3u8toMP3_0.1.1_linux > m3u8toMP3
```

Give execute permissions to the binary:

```shell
chmod +x ./m3u8toMP3
```

Use the following syntax to convert your m3u8 files to MP3. 
You can use both URLs and local paths:

```shell
./m3u8toMP3 "https://some-site.com/file.m3u8"
./m3u8toMP3 "<path/to/file.m3u8>"
```

If you want to specify a name for the output MP3 file, 
add one more argument to the command:

```shell
./m3u8toMP3 "<path/to/file.m3u8>" "./output.mp3"
```

If you want to use the program without directory path, you can, for example,
append PATH variable with the current path, or move the binary to 
/usr/local/bin:

```shell
mv ./m3u8toMP3 /usr/local/bin/m3u8toMP3
```

And then you can run the program anywhere:

```shell
m3u8toMP3 "https://some-site.com/index.m3u8"
```


## Installation and usage as a python script

Install the package using your favorite package manager. 
For example, using pip:

```shell
pip install m3u8toMP3
```

To run the script from the command line, use the following syntax:

```shell
python -m m3u8toMP3 "<path_to_m3u8_file>" "<path_to_save_mp3_file"
```

To use the script in your code, 
you need to import the **convert_m3u8_to_mp3** function:

```python
from m3u8toMP3 import convert_m3u8_to_mp3
...

async def main():
    await convert_m3u8_to_mp3("path/to/file.m3u8", "path/to/output.mp3")
    ...
```

If you want to work with in-memory bytes objects, use the class M3u8Converter:
```python
from m3u8toMP3 import M3u8Converter
...

async def main():
    mp3_bytes = await M3u8Converter.convert_to_mp3(m3u8_bytes)
    ...
```