from api_client import KeyAPI

# Run as: ./venv/bin/python3 client.py 

username = "admin"
password = "admin"
host = "http://127.0.0.1:9080/restconf"

def main():
    # Create an instance of the API client
    api = KeyAPI(host, username, password)

    # Create a new record
    api.create_top("John", "Doe", 30, 42)

    # Get the full record
    record = api.get_top("John", "Doe")
    print(record)

    # Update the age
    api.update_top("John", "Doe", age=31)

    # Get the age
    age = api.get_age("John", "Doe")
    print(f"Age: {age}")

    # Set the shoe size
    api.set_shoe_size("John", "Doe", 43)

    # Get the shoe size
    shoe_size = api.get_shoe_size("John", "Doe")
    print(f"Shoe size: {shoe_size}")

    # Delete the record
    api.delete_top("John", "Doe")

if __name__ == "__main__":
    main()
