import subprocess

url = None
while not url or result.returncode == 1:
    url = input('YouTube url: ')
    downloader = f'python [Path\\to\\youtube_dl] -x --audio-format mp3 {url} -o "/Download/%(uploader)s - %(title)s.%(ext)s" --ffmpeg-location [Path\\to\\ffmpeg]'
    result = subprocess.run(downloader)

input('Enter to exit: ')
