from flask import Flask, request, make_response, jsonify
import base64

users: list[dict] = [
    {
        "username": "admin",
        "password": "admin01",
        "rights": {
            "add_citzen": True,
            "view_citzens": True,
            "edit_citzen": True,
            "delete_citzen": True
        }
    },
    {
        "username": "basic",
        "password": "basic01",
        "rights": {
            "add_citzen": False,
            "view_citzens": True,
            "edit_citzen": False,
            "delete_citzen": False
        }
    },
]

def verify_auth() -> dict | None:
    """
    Verifies the authentication by extracting and decrypting the credentials 
    from the request packet. Returns the user dictionary if credentials match.
    """
    enc_auth_header: str = request.headers.get('Authorization')
    enc_auth_data: str = enc_auth_header[6:]
    dec_auth_data: str = base64.b64decode(enc_auth_data).decode('utf-8')
    input_username, input_password = dec_auth_data.split(':')

    for user in users:
        if input_username == user["username"] and input_password == user["password"]:
            return user  # Return user dict if found
    return None

citzens: list[dict] = list()

api: Flask = Flask(__name__)

def check_permissions(user: dict, action: str) -> bool:
    """
    Checks if the authenticated user has the required permission for the action.
    """
    return user["rights"].get(action, False)


# Operation 1: Add citizen ----------------------------------------------------
@api.route(rule='/add_citzen', methods=['POST'])
def add_citzen() -> None:
    """
    Adds a new citizen to the list if the authenticated user has permission.
    """
    user = verify_auth()
    if not user:
        return make_response(jsonify({"Msg": "Authentication failed"}), 401)
    
    if not check_permissions(user, "add_citzen"):
        return make_response(jsonify({"Msg": "Permission denied"}), 403)

    if request.headers.get('Content-Type') == 'application/json':
        new_id = 0 if not citzens else int(citzens[-1]["id"]) + 1
        request.json["id"] = str(new_id)
        citzens.append(request.json)
        return make_response(jsonify({"Msg": "Citizen added", "id": request.json["id"]}), 200)

# ----------------------------------------------------------------------------


# Operation 2: View citizens -------------------------------------------------
@api.route('/view_citzens', methods=['GET'])
def view_citzens() -> None:
    """
    Returns the list of citizens if the authenticated user has permission.
    """
    user = verify_auth()
    if not user:
        return make_response(jsonify({"Msg": "Authentication failed"}), 401)
    
    if not check_permissions(user, "view_citzens"):
        return make_response(jsonify({"Msg": "Permission denied"}), 403)

    return jsonify(citzens)
# ----------------------------------------------------------------------------


# Operation 3: Edit citizen --------------------------------------------------
@api.route('/edit_citzen/<id>', methods=['PUT'])
def edit_citzen(id: str):
    """
    Edits the details of a citizen by their ID if the authenticated user has permission.
    """
    user = verify_auth()
    if not user:
        return make_response(jsonify({"Msg": "Authentication failed"}), 401)
    
    if not check_permissions(user, "edit_citzen"):
        return make_response(jsonify({"Msg": "Permission denied"}), 403)

    updated_data = request.json
    for citzen in citzens:
        if citzen["id"] == id:
            citzen.update(updated_data)
            return make_response(jsonify({"Msg": "Citizen values successfully edited"}), 200)
    
    return make_response(jsonify({"Msg": "Citizen ID not found"}), 404)

# ----------------------------------------------------------------------------


# Operation 4: Delete citizen ------------------------------------------------
@api.route('/delete_citzen/<id>', methods=['DELETE'])
def delete_citzen(id: str):
    """
    Deletes a citizen by their ID if the authenticated user has permission.
    """
    user = verify_auth()
    if not user:
        return make_response(jsonify({"Msg": "Authentication failed"}), 401)
    
    if not check_permissions(user, "delete_citzen"):
        return make_response(jsonify({"Msg": "Permission denied"}), 403)

    for index, citzen in enumerate(citzens):
        if citzen["id"] == id:
            citzens.pop(index)
            return make_response(jsonify({"Msg": "Citizen successfully deleted"}), 200)
    
    return make_response(jsonify({"Msg": "Citizen ID not found"}), 404)

# ----------------------------------------------------------------------------


# Start the Flask server -----------------------------------------------------
if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8085, ssl_context='adhoc')
# ----------------------------------------------------------------------------
