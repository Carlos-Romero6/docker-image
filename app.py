from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    text = "Leroy es un desgraciado uwu"
    videourl = "static/video.mp4"
    return render_template("index.html", text=text, videourl=videourl)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
