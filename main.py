from flask import Flask, render_template, url_for, request, redirect, session, send_file
from backend import Downloader

import os

app = Flask(__name__)
downloader = Downloader()
app.secret_key = "37825789567878456784867878680"

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
        if "video_button" in request.form:
            quality_list = request.form["video_button"].split(",")
            video = downloader.find_video(quality_list[0], quality_list[1])
            fname = downloader.download(video)
            return send_file(fname, as_attachment=True)
        elif "audio_button" in request.form:
            video = downloader.find_audio(request.form["audio_button"])
            fname = downloader.download(video)
            return send_file(fname, as_attachment=True)
        elif "audiovideo_button" in request.form:
            quality_list = request.form["audiovideo_button"].split(",")
            video = downloader.find_audio_videos(quality_list[0], quality_list[1], quality_list[2])
            fname = downloader.download(video)
            return send_file(fname, as_attachment=True)
        else:
            url = request.form["ur"]
            session["url"] = url
            downloader.set_url(session["url"])
            videos = downloader.get_videos()
            audios = downloader.get_audios()
            audiovideos = downloader.get_audio_videos()
            title = downloader.get_title()
            thumbnail = downloader.get_thumbnail()
            views = downloader.get_views()
            duration = downloader.get_duration()

            print(duration)

            return render_template("index.html", url=session["url"], videos=videos, audios=audios, audiovideos=audiovideos, title=title, thumbnail=thumbnail, views=views, duration=duration)
    else:
        if "url" in session:
            return render_template("index.html", url=session["url"])
        else:
            return render_template("index.html", url="")
        
@app.route("/about")
def about():
    return "about"

@app.route("/contact")
def contact():
    return "contact"

if __name__ == "__main__":
    app.run(debug=True)

