import requests

# Prompt: 
# Create a Python API that implements the API described in the Swagger JSON file.
#
# This `KeyAPI` class provides methods to interact with the API endpoints defined
# in the Swagger JSON. Here's a brief explanation of the methods:
#
# - `__init__(self, base_url, username, password)`: Initializes the API client with the base URL,
#   username, and password for authentication.
# - `get_top(self, name, surname)`: Retrieves the top information for the given name and surname.
# - `create_top(self, name, surname, age, shoe_size)`: Creates a new top entry with the provided details.
# - `update_top(self, name, surname, age=None, shoe_size=None)`: Updates the top information for the given name and surname.
# - `delete_top(self, name, surname)`: Deletes the top information for the given name and surname.
# - `get_age(self, name, surname)`: Retrieves the age for the given name and surname.
# - `set_age(self, name, surname, age)`: Sets the age for the given name and surname.
# - `get_shoe_size(self, name, surname)`: Retrieves the shoe size for the given name and surname.
# - `set_shoe_size(self, name, surname, shoe_size)`: Sets the shoe size for the given name and surname.

class KeyAPI:

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = (username, password)
        self.headers = {
            'Accept': 'application/yang-data+json',
            'Content-Type': 'application/yang-data+json'
        }

    def get_top(self, name, surname):
        url = f"{self.base_url}/data/key:top={name},{surname}"
        response = requests.get(url, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_top(self, name, surname, age, shoe_size):
        url = f"{self.base_url}/data"
        data = {
            "key:top": [{
                "name": name,
                "surname": surname,
                "age": age,
                "shoe-size": shoe_size
            }]
        }
        response = requests.post(url, auth=self.auth, headers=self.headers, json=data)
        response.raise_for_status()
        return response.status_code == 201

    def update_top(self, name, surname, age=None, shoe_size=None):
        url = f"{self.base_url}/data/key:top={name},{surname}"
        data = {"key:top": [{}]}
        if age is not None:
            data["key:top"][0]["age"] = age
        if shoe_size is not None:
            data["key:top"][0]["shoe-size"] = shoe_size
        response = requests.patch(url, auth=self.auth, headers=self.headers, json=data)
        response.raise_for_status()
        return response.status_code == 204

    def delete_top(self, name, surname):
        url = f"{self.base_url}/data/key:top={name},{surname}"
        response = requests.delete(url, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.status_code == 204

    def get_age(self, name, surname):
        url = f"{self.base_url}/data/key:top={name},{surname}/age"
        response = requests.get(url, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()["key:age"]

    def set_age(self, name, surname, age):
        url = f"{self.base_url}/data/key:top={name},{surname}/age"
        data = {"key:age": age}
        response = requests.put(url, auth=self.auth, headers=self.headers, json=data)
        response.raise_for_status()
        return response.status_code in (201, 204)

    def get_shoe_size(self, name, surname):
        url = f"{self.base_url}/data/key:top={name},{surname}/shoe-size"
        response = requests.get(url, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()["key:shoe-size"]

    def set_shoe_size(self, name, surname, shoe_size):
        url = f"{self.base_url}/data/key:top={name},{surname}/shoe-size"
        data = {"key:shoe-size": shoe_size}
        response = requests.put(url, auth=self.auth, headers=self.headers, json=data)
        response.raise_for_status()
        return response.status_code in (201, 204)
