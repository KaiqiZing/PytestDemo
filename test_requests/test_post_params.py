import json

import requests

params = {
    "shouji": "13456755448",
    "appkey": "0c818521d38759e1"
}
r = requests.post('https://api.binstd.com/shouji/query', params=params)

json_data = r.json()
loads_data_json = json.dumps(json_data)
print(loads_data_json[status])
