from pytube import YouTube
import ffmpeg

class Downloader:
    def __init__(self):
        pass

    def set_url(self, url):
        self.youtube = YouTube(url)

    def get_videos(self):
        return [stream for stream in self.youtube.streams.filter(only_video=True)]
    
    def get_audios(self):
        return [stream for stream in self.youtube.streams.filter(only_audio=True)]
    
    def get_audio_videos(self):
        return [stream for stream in self.youtube.streams.filter(progressive=True)]
    
    def combine_audio_video(self, audio, video):
        pass
        #video_stream = ffmpeg.input(video.download().split("//")[-1])
        #audio_stream = ffmpeg.input(audio.download().split("//")[-1])
        #ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()