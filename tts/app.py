from synthesize import text_to_mp3
from htmlscrap import html_to_text

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    url = request.form['url']
    
    if url is not None:
        return html_to_text(url)
    
    return f'No text found!!'

if __name__ == "__main__":
    # Used when running locally only. When deploying to Cloud Run,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host="localhost", port=8080, debug=True)
    