from flask import Flask, render_template, url_for, request, redirect, session, send_file
from backend import Downloader

import os

app = Flask(__name__)
downloader = Downloader()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form["ur"]
        downloader.set_url(url)
        videos = downloader.get_videos()
        audios = downloader.get_audios()
        audiovideos = downloader.get_audio_videos()

        print(videos)
        print(audios)
        print(audiovideos)

        return render_template("index.html")
    else:
        return render_template("index.html")
        
@app.route("/about")
def about():
    return "about"

@app.route("/contact")
def contact():
    return "contact"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

