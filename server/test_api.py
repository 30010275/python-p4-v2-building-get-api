import requests
from pprint import pprint

base_url = "http://localhost:5555"

def test_endpoint(endpoint):
    try:
        response = requests.get(f"{base_url}{endpoint}")
        print(f"\nTesting {endpoint}:")
        print(f"Status Code: {response.status_code}")
        print("Response:")
        pprint(response.json())
    except Exception as e:
        print(f"Error testing {endpoint}: {str(e)}")

if __name__ == "__main__":
    test_endpoint("/games")
    test_endpoint("/games/1")
    test_endpoint("/games/users/1")
