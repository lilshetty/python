import requests
import json
res=requests.get('https://goweather.herokuapp.com/weather/bangalore')
data=json.loads(res.text)
#print(data)
temp=data.get('temperature')
wind=data.get('wind')
desc=data.get('description')
print(temp)
print(wind)
print(desc)
