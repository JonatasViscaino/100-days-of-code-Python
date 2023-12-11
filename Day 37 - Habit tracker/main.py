import requests

pixela_user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "YOUR_TOKEN",
    "username": "YOUR_USERNAME",
    "agreeTermsOfService": "yes/no",
    "notMinor": "yes/no",
}

# Creating a user
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = "https://pixe.la/v1/users/tinhas99/graphs"

