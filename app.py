'''TubeLoad server'''
import os
import traceback
from flask import Flask, request, send_from_directory
from downloader import Downloader

app = Flask(__name__)
downloader = Downloader()


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/static/<path:path>')
def static_folder(path):
    return app.send_static_file(path)


@app.route('/images/<path:path>')
def images(path):
    return app.send_static_file('images/' + path)


@app.route('/version')
def get_version():
    with open ('static/version.txt', 'r') as version_file:
        return version_file.read()


@app.route('/download')
def download():
    song_id = request.args['id']
    
    if song_id.find('.') == -1:
        try:
            downloader.download(song_id)
        except Exception as e:
            return traceback.format_exc(), 500
        return send_from_directory(downloader.songs_path, song_id + '.mp3', as_attachment=True)
    else:
        return 'Invalid id', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0')
