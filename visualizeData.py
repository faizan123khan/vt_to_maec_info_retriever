import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/file/report'


params = {'apikey': '7a11ef9031accd2ab410aae42525bcfc0d6b6014eea91920a0481dfbc2be4648',
          'resource': '2d121569e955eb2022ee8eddf21c9975', 'allinfo': '1'}

response = requests.get(url, params=params)
jsonresponse = response.json()
with open('2d121569e955eb2022ee8eddf21c9975.json', 'w') as fp:
    json.dump(jsonresponse, fp, indent=4)