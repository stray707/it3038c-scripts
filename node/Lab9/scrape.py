import requests
import json

response = requests.get('http://localhost:3000/')

if response.status_code == 200:
    # Parse the JSON data
    data = json.loads(response.text)

    # Iterate through the JSON data and print the information
    for widget in data:
        name = widget["name"]
        color = widget["color"]
        print(f"{name.capitalize()} is {color}.")

else:
    print("Failed to fetch data from the server.")
