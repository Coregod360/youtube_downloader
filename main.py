import typer
from typing import Optional
import pytube
from rich.progress import track
import ffmpeg
import os
#remove this
import time

app = typer.Typer(help='CLI app for downloading and clipping YouTube videos. Offers multiple presets to convert videos into suitable formats for popular platforms through ffmpeg.')

# Change more tradional CLI app add -D / --download -C --clip flags for download and clip
# Add -h flag for help


@app.command()
def download (url: str = typer.Argument("", help="Url for a YouTube video to download")):
    """
    Downloads a full YouTube video in the highest resolution available. 
    """

    yt = pytube.YouTube(
        url,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        use_oauth=True,
        allow_oauth_cache=True
    )
    yt.streams.get_highest_resolution().download(
        # Make configurable by user
        output_path="/home/kensix/Videos/YT downloads/",
        filename=yt.title + ".mp4",
        skip_existing=True
    )


@app.command()
def clip (
    url: str = typer.Argument("", help="Url for a YouTube video to clip" ),
    start_time: Optional[str] = typer.Option(None, '--start', help="[Optional] Start time for clip (hh:mm:ss)"),
    end_time: Optional[str] = typer.Option(None, '--end', help="[Optional] End time for clip (hh:mm:ss)"),
    out_file: Optional[str] = typer.Option(None, '--file', help='[Optional] Output file name, For spaces in your filename use quotes example: "my output file"'),
    preset: Optional[str] = typer.Option(None, '--preset', help="[Optional] Preset for ffmpeg conversion [ 4chan, discord, medium-quality, full-quality ]")
    ):
    """
    Clips a YouTube video between a user specified start and end time. takes optional arguments 
    for --start_time and --end_time to specify the clip lenght. --out_file to specify a 
    name for the output file. --preset will specify one of the presets that converts the video to
    a suitable format and file size for popular platforms. 
    
    Presets
        CHANGE THESE TO THE CORRECT INFO
        4chan: Webm format, 480p, 1.5mbps, 30fps
        discord: Mp4 format, 480p, 1.5mbps, 30fps
        medium-quality: Mp4 format, 720p, 3mbps, 30fps
        full-quality: Mp4 format, 1080p, 5mbps, 30fps
         
    
    If no arguments are provided, the user will be prompted for the required information. 
    """
    if(start_time == None):
       start_time = typer.prompt(f"Enter start time for clip (hh:mm:ss)")
    
    if(end_time == None):
        end_time = typer.prompt(f"Enter end time for clip (hh:mm:ss)") 
    
    if(out_file == None):
        out_file = typer.prompt(f"Enter output file name") 
    
    if(preset == None):
        preset = ["4chan", "discord", "medium-quality", "full-quality"]
    
    yt = pytube.YouTube(
        url,
        on_progress_callback=progress_func,
        on_complete_callback=complete_func,
        use_oauth=True,
        allow_oauth_cache=True
    )
    yt.streams.get_highest_resolution().download(
        output_path="/home/kensix/Videos/YT downloads/",
        filename=yt.title + ".mp4",
        skip_existing=True
    )

    source_file = (f'/home/kensix/Videos/YT downloads/{yt.title}.mp4')

    typer.echo(ffmpeg_trim(source_file, start_time, end_time, out_file, preset))
    

    # Delete original file
    # os.remove(source)


def ffmpeg_trim(source, start_time, end_time, out_file, preset):
    #Make configurable by user
    base_path = "/home/kensix/Videos/YT downloads/"
    
    #CAlculate file size
    # FFMPEG PROBE TO GET THE SOURCE FILE SIZE
    # FFMPEG PROBE TO GET THE DURATION OF THE SOURCE FILE
    # LEAVES ROOM FOR INTERPERETATION ON THE LOWER RESOLUTIONS
    #DIVIDE SIZE BY LENGHT TO GET SIZE PER SECOND
    #IF SIZE PER SECOND FOR DURATION LARGER THAN MAX SIZE FOR PRESET
    #THEN SCALE DOWN TO RESOLUTION 
    # NEED SOME DATA ON THE SIZE OF THE DIFFERENT RESOLUTIONS




    #if(preset == "4chan"):
        # Maximum file size is 4096KB for /gif/ and 6144KB for /wsg/.
        # Maximum duration is 300 seconds (5 minutes).
        # Maximum resolution is 2048x2048 pixels.
        # No audio streams except on /gif/ and /wsg/. (use -an)
        # Vp9 codec

    #if(preset == "discord"):
        # Maximum file size is 8MB.
        # No maximum duration.
        # No maximum resolution.
        # Audio is allowed.
    
    #if(preset == "medium-quality"):
        # scale down to 720p

    #if(preset == "full-quality"):
        #maintain original quality

    ext = ".mp4"
    out_file = base_path + out_file + ext
    
    input_stream = ffmpeg.input(source)
    pts = "PTS-STARTPTS"
    
    video = input_stream.trim(start=start_time, end=end_time).setpts(pts)
    audio = (input_stream
            .filter("atrim", start=start_time, end=end_time)
            .filter("asetpts", pts)
    )

    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    output_stream = ffmpeg.output(video_and_audio, out_file, format="mp4")
    output_stream.run()
    return('Done')


def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    for bytes_downloaded in track(range(total_size), description="Downloading..."):
        continue
    

def complete_func(stream, file_handle):
    print("Download complete")
    

if __name__ == "__main__":
    app()
