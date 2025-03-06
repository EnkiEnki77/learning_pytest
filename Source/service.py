import requests

database = {
    1: "Enki",
    2: "Alice",
    3: "Bob",
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.HTTPError()