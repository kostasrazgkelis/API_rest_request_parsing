import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes': 100, 'name': 'kostas', 'views': 2000},
        {'likes': 3000, 'name': 'nikos', 'views': 1300},
        {'likes': 30, 'name': 'pamblp', 'views': 530}]


response = requests.patch( BASE + "/video/1" , {'name':'asdasdasd'})
print( response.json())
