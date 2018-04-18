'''Downloader'''
import os
import youtube_dl

OPTIONS = {
    'nocheckcertificate': True,
    'format': 'worstaudio/worst',
    'extractaudio' : True,  # only keep the audio
    'audioformat' : "mp3",  # convert to mp3
    'outtmpl': 'songs/%(id)s.m4a',  # name the file the ID of the video
    'noplaylist' : True,  # only download single song, not playlist
    'writethumbnail': True,
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        },
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'},
    ],
}

class Downloader:
    '''YouTube downloader'''
    def __init__(self):
        self.youtube_url = 'https://www.youtube.com/watch?v='
        self.songs_path = './songs/'
        self.songs = []
        self.cache_size = 200

        if not os.path.exists(self.songs_path):
            os.mkdir(self.songs_path)

    def download(self, song_id):
        '''downloading a song from YouTube'''
        song_path = 'songs/' + song_id + '.mp3'

        if not os.path.exists(song_path):
            youtube_downloader = youtube_dl.YoutubeDL(OPTIONS)
            youtube_downloader.download([self.youtube_url + song_id])
            self.songs.append(song_id)
            self.__remove_last_song()
    
    def __remove_last_song(self):
        if len(self.songs) > self.cache_size:
            os.remove(self.songs_path + self.songs[0] + '.mp3')
            self.songs = self.songs[1:]
