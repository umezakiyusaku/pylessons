import requests as req
import json
url='http://api.open-notify.org/iss-now.json'
res=req.get(url)
data=json.loads(res.text)
pos=data['iss_position']
print('ISS緯度度は{},経度は{}'.format(pos['latitude'],pos['longitude']))
