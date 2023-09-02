import requests
import time


# Set your JWT token here (replace with the one you got from the /auth endpoint)
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZmxhc2tBcHAifQ.MBFpdWRktzCb8Dfim0mJsu7wwW_2Gv5xzm4hOj2PX2w"
headers = {'Authorization': f'Bearer {jwt_token}'}

# Replace with your actual API endpoint URL
api_url = 'http://localhost:5000/protected'

# specify the number of requests to be made
num_requests = 10

for i in range(num_requests):
    response = requests.get(api_url, headers=headers)
    print(f'Request {i + 1} - Status Code: {response.status_code}')
    print(f'Response Content: {response.text}')
    time.sleep(1)