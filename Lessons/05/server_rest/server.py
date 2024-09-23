from flask import Flask, jsonify
import requests

api = Flask(__name__)

# Route to get all todos
@api.route('/todos', methods=['GET'])
def get_todos() -> dict:
    # Make an API request to get the todos
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response directly
        return jsonify(response.json())
    else:
        # Handle the error if the request failed
        return {"error": "Failed to fetch todos"}, response.status_code

# Route to get a specific todo by 
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id: int) -> dict:
    # Make an API request to get a specific todo by its ID
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the JSON response for the specific todo
        return jsonify(response.json())
    else:
        # Handle the error if the request failed (e.g., todo not found)
        return {"error": f"Failed to fetch todos/{id}"}, response.status_code

# Run the Flask development server on host "0.0.0.0" and port 8085
if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8085)
