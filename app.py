from flask import Flask, jsonify
import pyramid

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pyramid/<value>", methods=["GET"])
def pyramid_request(value):
    resp = pyramid.is_pyramid(value)
    return jsonify(value=value, is_pyramid=resp)


if __name__ == "__main__":
    app.run()
