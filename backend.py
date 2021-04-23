from pytube import YouTube
import datetime
import os

class Downloader:
    def __init__(self):
        pass

    def set_url(self, url):
        self.youtube = YouTube(url)

    def get_videos(self):
        return [stream for stream in self.youtube.streams.filter(only_video=True, video_codec="vp9")]
    
    def get_audios(self):
        return [stream for stream in self.youtube.streams.filter(only_audio=True)]
    
    def get_audio_videos(self):
        return [stream for stream in self.youtube.streams.filter(progressive=True)]
    
    def find_video(self, resolution, fps):
        video = None

        for stream in self.get_videos():
            if str(stream.resolution) == resolution:
                if str(stream.fps) == fps:
                    video = stream
                    break
        
        return video
    
    def find_audio(self, bitrate):
        audio = None

        for stream in self.get_audios():
            print(bitrate)
            print(stream.abr)
            if str(stream.abr) == bitrate:
                audio = stream
                break
        
        print(audio)
        return audio
    
    def find_audio_videos(self, resolution, fps, bitrate):
        video = None

        for stream in self.get_audio_videos():
            if str(stream.resolution) == resolution:
                if str(stream.fps) == fps:
                    if str(stream.abr) == bitrate:
                        video = stream
                        break
        
        print(video)
        return video
    
    def download(self, video):
        print(video)
        local_path = video.download()
        fname = local_path.split("//")[-1]

        return fname
    
    def get_title(self):
        return self.youtube.title
    
    def get_thumbnail(self):
        return self.youtube.thumbnail_url

    def get_views(self):
        return self.youtube.views

    def get_duration(self):
        return str(datetime.timedelta(seconds=self.youtube.length))
