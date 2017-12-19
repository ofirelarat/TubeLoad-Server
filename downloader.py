'''Downloader'''
import os
import youtube_dl

OPTIONS = {
            'format': 'bestaudio/best',
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
        self.songs_file_path = self.songs_path + 'songs.txt'

    def download(self, song_id):
        '''downloading a song from YouTube'''
        song_path = 'songs/' + song_id + '.mp3'

        if not os.path.exists(song_path):
            youtube_downloader = youtube_dl.YoutubeDL(OPTIONS)
            youtube_downloader.download([self.youtube_url + song_id])
            self.__update_songs_file(song_id)

    def __update_songs_file(self, song_name):
        song_names = self.__read_songs_file()

        if len(song_names) > 100:
            os.remove(song_names[0])
            song_names.pop(0)

        song_names.append(song_name)
        self.__write_songs_file(song_names)

    def __read_songs_file(self):
        with open(self.songs_file_path, 'r') as songs_file:
            return songs_file.readlines()

    def __write_songs_file(self, song_names):
        with open(self.songs_file_path, 'w') as songs_file:
            for song_name in song_names:
                songs_file.write(song_name)
