#TO GET MSMARCO PASSAGE
# wget https://msmarco.z22.web.core.windows.net/msmarco/dev_v2.1.json.gz

import requests
import gzip
import json

getWebsite = requests.get(" https://msmarco.z22.web.core.windows.net/msmarco/dev_v2.1.json.gz")

json_data = gzip.decompress(getWebsite.content)

newFormat = json.loads(json_data)

print(data)



