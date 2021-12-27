import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name":"Kimani", "views":10000, "likes":2000},
    {"name":"Njeri", "views":10500, "likes":2090},
    {"name":"Githae", "views":89000, "likes":2700}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.delete(BASE + "video/2")
print(response)

input()

response = requests.get(BASE + "video/0")
print(response.json())
