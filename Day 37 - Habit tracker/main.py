import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_CREATED_TOKEN"
GRAPH_ID = "YOUR_GRAPH_NAME"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes/no",
    "notMinor": "yes/no",
}

# Creating a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Program Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

# Creating a Habit Pixel in graph
pixelcreation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today_date,
    "quantity": "2",
}

response = requests.post(url=pixelcreation_endpoint, headers=graph_headers, json=pixel_data)
print(response.text)

# Update a Habit pixel in graph
day_update = "20231212"

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_update}"

pixel_update = {
    "quantity": "3"
}

# response = requests.put(url=update_endpoint, headers=graph_headers, json=pixel_update)
# print(response.text)

# Delete a Habit pixel data in graph
day_delete = "20231212"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_delete}"

# response = requests.delete(url=delete_endpoint, headers=graph_headers)
# print(response.text)
