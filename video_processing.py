import ffmpeg
import os


def ffmpeg_trim(source, start_time, end_time, out_file, preset):
    #Make configurable by user
    # base_path = "/home/kensix/Videos/YT downloads/" !!!!
    
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
    # out_file = base_path + out_file + ext
    out_file = "newfile.mp4"
    

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
