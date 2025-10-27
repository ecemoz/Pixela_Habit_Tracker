import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "ecemnurozen"
TOKEN = "1234567890ecemnurozen"
GRAPH_ID = "graph1"

user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response_graph.text)

today = datetime.now()
pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? ")
}


#response_create_pixel = requests.post(url=f"{graph_endpoint}/{GRAPH_ID}", json=pixel, headers=headers)
#print(response_create_pixel.text)

update_pixel = {
    "quantity": "5"
}
#response_update_pixel = requests.put(url=f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}", json=update_pixel, headers=headers)
#print(response_update_pixel.text)

delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response_delete_pixel = requests.delete(url=delete_endpoint, headers=headers)
#print(response_delete_pixel.text)
