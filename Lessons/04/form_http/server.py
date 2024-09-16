from flask import Flask, render_template, request

# List of example users with email, codice fiscale, and password
example_users: list[list[str]] = [
    ["mario.rossi@example.com", "RSSMRA80A01H501U", "P@ssw0rd123"],
    ["luca.bianchi@example.com", "BNCGIO85C12F205S", "Luca2023!"],
    ["anna.verdi@example.com", "VRDANN90D13L219M", "Anna_V!456"]
]

# Create an instance of the Flask class
api = Flask("__name__")

# Define a route for the root URL ("/") that responds to GET requests
@api.route('/', methods=['GET'])
def index():
    # Render and return the HTML template "index.html"
    return render_template("index.html")


# Route to handle registration form submission
@api.route('/registration', methods=['POST'])
def registration():
    # Get form data from the POST request
    email: str = request.form["email"]
    cf: str = request.form["cf"]
    password: str = request.form["psw"]

    # Create a list from the input data
    input_user: list[str] = [email, cf, password]

    # Check if the input user is already in the example_users list
    if input_user in example_users:
        # If the user does not exist, render the success page
        return render_template("reg_ok.html")
    else:
        # If the user exists, render the failure page
        return render_template("reg_ko.html")

# Run the Flask development server on host "0.0.0.0" and port 8085
if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8085)
