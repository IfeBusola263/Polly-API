import requests
from typing import List, Dict, Any

BASE_URL = "http://localhost:8000"

def register_user(username: str, password: str) -> Dict[str, Any]:
    """
    Registers a new user via the /register endpoint.

    Args:
        username: The username for the new user.
        password: The password for the new user.

    Returns:
        A dictionary containing the registered user's information (id, username)
        or an error message.
    """
    url = f"{BASE_URL}/register"
    headers = {"Content-Type": "application/json"}
    payload = {"username": username, "password": password}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def get_paginated_polls(skip: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    """
    Fetches paginated poll data from the /polls endpoint.

    Args:
        skip: The number of items to skip (for pagination).
        limit: The maximum number of items to return (for pagination).

    Returns:
        A list of dictionaries, each representing a poll.
    """
    url = f"{BASE_URL}/polls"
    params = {"skip": skip, "limit": limit}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

if __name__ == "__main__":
    # Example Usage:
    # You might need to run the Polly-API server (main.py) first for these examples to work.

    # 1. Register a new user
    print("Attempting to register a new user...")
    try:
        registered_user = register_user("testuser", "testpassword")
        print(f"User registered successfully: {registered_user}")
    except requests.exceptions.HTTPError as e:
        print(f"Error registering user: {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred during registration: {e}")

    print("\nAttempting to register an existing user (should fail)...")
    try:
        registered_user = register_user("testuser", "testpassword")
        print(f"User registered successfully: {registered_user}")
    except requests.exceptions.HTTPError as e:
        print(f"Error registering user (expected): {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred during registration: {e}")

    # 2. Fetch paginated poll data
    print("\nFetching paginated poll data (skip=0, limit=2)...")
    try:
        polls = get_paginated_polls(skip=0, limit=2)
        print(f"Fetched polls: {polls}")
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching polls: {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred during poll fetching: {e}")

    print("\nFetching paginated poll data (skip=1, limit=1)...")
    try:
        polls = get_paginated_polls(skip=1, limit=1)
        print(f"Fetched polls: {polls}")
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching polls: {e.response.json()}")
    except Exception as e:
        print(f"An unexpected error occurred during poll fetching: {e}")