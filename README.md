# m3u8toMP3 

Based on **@asvatov/m3u82mp3** simple module, the program converts m3u8 
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


## Installation and usage as a python script
