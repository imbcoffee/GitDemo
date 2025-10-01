import os
import subprocess
from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)
MOVIE_FOLDER = "E:/Watch"

@app.route('/')
def index():
    movies = [f for f in os.listdir(MOVIE_FOLDER) if f.lower().endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    return render_template('index.html', movies=movies)

@app.route('/play/<path:filename>')
def play(filename):
    path = os.path.abspath(os.path.join(MOVIE_FOLDER, filename))
    if os.path.exists(path):
        subprocess.Popen([r"C:\Program Files\VideoLAN\VLC\vlc.exe", path])
    return redirect(url_for('index'))

@app.route('/movies/<path:filename>')
def serve_movie(filename):
    return send_from_directory(MOVIE_FOLDER, filename)

if __name__ == '__main__':
    app.run()

#just for gitdemo

#another change from USER B

# another from userB

#test main user in new develop branch