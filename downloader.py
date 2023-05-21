import yt_dlp
import json

def yld_download(url, job):
    # TODO: Add something like configparser to let user customize download path etc 
    basepath = "/home/kensix/deadNiggerStorage/Coding/youtube_downloader/output/"

    class MyLogger:
        def debug(self, msg):
            # For compatibility with youtube-dl, both debug and info are passed into debug
            # You can distinguish them by the prefix '[debug] '
            if msg.startswith('[debug] '):
                pass
            else:
                self.info(msg)

        def info(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            raise Exception(msg)


    # ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)
    def my_hook(d):
        final_filename  = d.get('info_dict').get('_filename')
        remaining_bytes = d.get('info_dict').get('filesize') - d.get('downloaded_bytes')
        print(remaining_bytes)
        print("download progress")
        if d['status'] == 'finished':
            print('Done downloading, now post-processing ...')
            print(final_filename)
            return final_filename


    if job == 'download':
        #highest quality download 
        ydl_opts = {
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'outtmpl': '%(title)s.%(ext)s', #TODO: Cant find a way to get a path variable to work here
            # 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }
        
    if job == 'clip':
        # Lower quality for faster download and less downscaling in ffmpeg
        ydl_opts = {
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'outtmpl': '%(title)s.%(ext)s',

            #TODO: Cant find a way to get a path variable to work here
            # 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)