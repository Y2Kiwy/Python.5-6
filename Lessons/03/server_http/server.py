from flask import Flask, render_template

# Create an instance of the Flask class. The string "__name__" is a conventional argument.
api = Flask("__name__")

# Define a route for the root URL ("/") that responds to GET requests
@api.route('/', methods=['GET'])
def index():
    # Render and return the HTML template "index.html"
    return render_template("index.html")

# Run the Flask development server on host "0.0.0.0" and port 8085
api.run(host="0.0.0.0", port=8085)
