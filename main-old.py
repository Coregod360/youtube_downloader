import typer
from typing import Optional
import downloader
from rich.progress import track
import os
import video_processing
#remove this
import time

app = typer.Typer(help='CLI app for downloading and clipping YouTube videos. Offers multiple presets to convert videos into suitable formats for popular platforms through ffmpeg.')

# Change more tradional CLI app add -D / --download -C --clip flags for download and clip
# Add -h flag for help

@app.command()
def update ():
    """
    Updates the app to the latest version along with all dependencies.
    """
    pass


@app.command()
def download (url: str = typer.Argument("", help="Url for a YouTube video to download")):
    """
    Downloads a full YouTube video in the highest resolution available. 
    """

    try:
        downloader.yld_download(url, "download")
    except Exception as e:
        typer.echo(f"Error: {e}")
        typer.echo(f"Exiting...")
        time.sleep(2)
        raise typer.Exit()


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
    
    # if(preset == None):
    #     preset = ["4chan", "discord", "medium-quality", "full-quality"]
    
    try:
        source_file = downloader.yld_download(url, "clip")
    except Exception as e:
        typer.echo(f"Error: {e}")
        typer.echo(f"Exiting...")
        time.sleep(2)
        raise typer.Exit()

    # source_file = (f'/home/kensix/Videos/YT downloads/title.mp4')
    print(source_file)
    
    typer.echo(video_processing.ffmpeg_trim(source_file, start_time, end_time, out_file, preset))
    

#  OLD PROGRESS BAR CODE
# def progress_func(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     for bytes_downloaded in track(range(total_size), description="Downloading..."):
#         continue
    

# def complete_func(stream, file_handle):
#     print("Download complete")
    

if __name__ == "__main__":
    app()
