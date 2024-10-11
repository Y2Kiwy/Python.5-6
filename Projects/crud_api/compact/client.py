import requests, requests.auth

# Functions used in the main script ------------------------------------------

def build_creds() -> requests.auth.HTTPBasicAuth:
    """
    Builds and returns authentication credentials using user input.
    """
    input_username: str = input("Enter username: ")
    input_password: str = input("Enter password: ")
    return requests.auth.HTTPBasicAuth(input_username, input_password)

def build_data() -> dict:
    """
    Prompts user to input citizen details and returns them as a dictionary.
    """
    name: str = input("Enter your name: ")
    surname: str = input("Enter your surname: ")
    birth: str = input("Enter your birth date: ")
    cf: str = input("Enter your cf: ")
    return {"nome": name, "cognome": surname, "nascita": birth, "cf": cf}

def choose_option() -> int:
    """
    Displays the menu and prompts the user to choose an operation.
    Returns the chosen option as an integer.
    """
    print("\nPlease select one of the following options:")
    print("1. Add citizen")
    print("2. Get citizens")
    print("3. Edit citizen")
    print("4. Remove citizen")
    print("5. Quit\n")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice (1 - 5): "))
            if choice in range(1, 6):
                return choice
            else:
                print("Invalid option, please choose a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number.")
# ----------------------------------------------------------------------------


# Start of the main script ---------------------------------------------------
if __name__ == "__main__":

    while True:
        # Authenticate user before allowing operation selection
        if not auth_creds.username or not auth_creds.password:
            auth_creds: requests.auth.HTTPBasicAuth = build_creds()
            continue

        BASE_URL: str = "https://127.0.0.1:8085"
        operation_id: int = choose_option()

        # Operation 1 -> Add a new citizen -----------------------------------
        if operation_id == 1:
            data: dict = build_data()
            response: requests.Response = requests.post(
                url=f"{BASE_URL}/add_citzen",
                json=data,
                auth=auth_creds,
                verify=False
            )
            if response.status_code == 200:
                print("Request successfully sent")
            else:
                print(f"Error: {response.status_code}")
        # --------------------------------------------------------------------

        # Operation 2 -> Get and display all citizens ------------------------
        elif operation_id == 2:
            response: requests.Response = requests.get(
                url=f"{BASE_URL}/view_citzens",
                auth=auth_creds,
                verify=False
            )
            if response.status_code == 200:
                print("Citizens:\n", response.json())
            else:
                print(f"Error: {response.status_code}")
        # --------------------------------------------------------------------

        # Operation 3 -> Edit an existing citizen by ID ----------------------
        elif operation_id == 3:
            input_id: str = input("\nEnter the user ID whose values you want to modify: ")
            print("Enter the new data value, leave blank to not modify:")
            updated_data: dict = build_data()
            response: requests.Response = requests.put(
                url=f"{BASE_URL}/edit_citzen/{input_id}",
                json=updated_data,
                auth=auth_creds,
                verify=False
            )
            if response.status_code == 200:
                print(f"Data successfully updated: {response.status_code}")
            else:
                print(f"Error: {response.status_code}")
        # --------------------------------------------------------------------

        # Operation 4 -> Delete a citizen by ID ------------------------------
        elif operation_id == 4:
            input_id: str = input("\nEnter the user ID to delete: ")
            response: requests.Response = requests.delete(
                url=f"{BASE_URL}/delete_citzen/{input_id}",
                auth=auth_creds,
                verify=False
            )
            if response.status_code == 200:
                print(f"Citizen successfully deleted: {response.status_code}")
            else:
                print(f"Error: {response.status_code}")
        # --------------------------------------------------------------------

        # Operation 5 -> Quit ------------------------------------------------
        elif operation_id == 5:
            break
        # --------------------------------------------------------------------

        # Wait for user input before showing the menu again
        input("\n")
# ----------------------------------------------------------------------------
