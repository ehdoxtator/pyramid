# pyramid

This is web service app written in response to Lindsey's request for a sample of my coding.

# Installation

1. To run the service, you will need to install flask.  From a command line, do 
`pip install flask`

Note: it's strongly recommended that you create a virtual environment or use pyenv to isolate the example from more useful Python configurations that may exist on your system.

2. Clone the pyramid repository from this repo with
`git clone https://github.com/ehdoxtator/pyramid.git`

3. Run the tests
`python test_pyramid.py`

Both tests should pass successfully.

4. Run the web app:
`python app.py`

Flask should fire up the web server, and you should see the messages:

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 
 5. Try it out on your web browser with
`http://127.0.0.1:5000/banana`

You should get back the following JSON payload:
`{"is_pyramid":true,"value":"banana"}`

Try out a non-pyramid conforming string:
`http://127.0.0.1:5000/bandana`

You should get back the following JSON payload:
`{"is_pyramid":false,"value":"bandana"}`

