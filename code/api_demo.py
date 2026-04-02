import os

import requests

# response = requests.get(
#     'https://oim.108122.xyz/words/random',
#     headers = {'X-Token': 'kamilakamila'})
# print(response.json())

# response = requests.get('https://oim.108122.xyz/mass')
# data = response.json()

# #print(data['name'])       # 'Massachusetts'
# #print(data['governor'])   # 'Maura Healey'

# for town in data['data'][:5]:
#     print(f"{town['name']}: pop {town['population']:,}")

# print(len(data))
# print(data.keys)
# print(type(data['data'])) # do this to explore data structure

# # seeing how many towns there are in the data
# towns = data['data']
# print(type(towns)) # list
# print(len(towns)) # 351  

# # find smallest town
# smallest = min(towns, key=lambda t: t['population'])
# print(f"Smallest town: {smallest['name']} with population {smallest['population']:,}")

# # find top 5 largest towns
# largest = sorted(towns, key=lambda t: t['population'], reverse=True)[:5]
# print("Top 5 largest towns:")
# for town in largest:
#     print(f"{town['name']}: pop {town['population']:,}")

# # find top 5 smallest towns
# smallest_5 = sorted(towns, key=lambda t: t['population'])[:5]
# print("Top 5 smallest towns:")
# for town in smallest_5:
#     print(f"{town['name']}: pop {town['population']:,}")

# requests.post('https://oim.108122.xyz/message', 
#               json={'message': 'Hello, from Kamila!'},
#               headers={'X-Token': 'kamilakamila'})

# Doesnt work: To delete the message from the server, use a DELETE request if the API supports it:
# response = requests.delete(
#     'https://oim.108122.xyz/message',
#     headers={'X-Token': 'kamilakamila'}
# )
# print(response.status_code)
# print(response.text)

# Also didnt work
# url = 'http://api.open-notify.org/astros.json'
# data = requests.get(url).json()
# print(f"There are currently {data['number']} people in space:")
# for person in data['people']:
#     print(f"{person['name']} on {person['craft']}") 

os.getenv('OPENWEATHER_API_KEY')
url = (f'https://api.openweathermap.org/data/2.5/weather?q=Boston,US&appid={os.getenv("OPENWEATHER_API_KEY")}&units=imperial')

print(url)
data = requests.get(url).json()
print(f"The current temperature in Boston is {data['main']['temp']}°F")

              