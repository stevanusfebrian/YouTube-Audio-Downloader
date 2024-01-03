# About
This repo contain simple python script for downloading YouTube Audio in mp3.

# Dependencies
to have the downloader run properly, you need to install 2 dependencies first:
- `youtube-dl`, see [here](https://github.com/ytdl-org/youtube-dl) and install it according to you OS.
- `ffmpeg`, see [here](https://ffmpeg.org/download.html) and download according to your OS, then you can choose what version of ffmpeg's build you wanna download. Latest is recommended.

ffmpeg is gonna used to convert the downloaded webm by youtube-dl as desired output audio file. ffmped folder can be placed in the same directory of your project.

# Code
1. Change two square brackets, `[Path\\to\\ffmpeg]` and `[Path\\to\\youtube_dl]` to your exact path of both `ffmpeg.exe` and `youtube_dl`'s folder location, example:
`C:\\Python311\\Lib\\site-packages\\youtube_dl`
and 
`C:\\Users\\...\\ffmpeg\\bin`


3. Inside `Extractor` Folder of youtube-dl package, modify `youtube.py` file as [this solution](https://stackoverflow.com/questions/75495800/error-unable-to-extract-uploader-id-youtube-discord-py#:~:text=I%20solved%20it%20temporarily%20(v2021.12.17)%20until%20there%27s%20a%20new%20update%2C%20by%20editing%20file) did to ignore the error of getting uploader_id for some youtube videos.

Thanks.
