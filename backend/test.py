import requests
import json

# The URL of your FastAPI endpoint
url = "http://localhost:8000/chat/summary"

# The JSON payload (the same data you passed with -d)
payload = {
    "history": [
        {
      "role": "user",
      "parts": "I'm looking for a friend to talk to about my new business idea."
    },
    {
      "role": "model",
      "parts": "Oh, that's exciting! Tell me all about it. What kind of business is it?"
    },
    {
      "role": "user",
      "parts": "It's an online store selling personalized t-shirts."
    },
    {
      "role": "model",
      "parts": "That sounds wonderful! I'm sure you'll be a great entrepreneur."
    }
    ],
    "character_id": "gangadhar"
}

# The headers for the request
headers = {
    "Content-Type": "application/json"
}

try:
    # Make the POST request
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    response.raise_for_status()  # This will raise an HTTPError if the response status is a client or server error

    # Print the JSON response from the server
    print(response.json())

except requests.exceptions.RequestException as e:
    # Handle any errors that occur during the request
    print(f"An error occurred: {e}")