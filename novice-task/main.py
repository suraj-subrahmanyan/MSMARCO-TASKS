#TO GET MSMARCO PASSAGE
# wget https://msmarco.z22.web.core.windows.net/msmarco/dev_v2.1.json.gz

import requests
import gzip
import json

getMSMARCO = requests.get("https://msmarco.z22.web.core.windows.net/msmarco/dev_v2.1.json.gz")

jsonData = gzip.decompress(getMSMARCO.content)

jsonFormat = json.loads(jsonData)

print(jsonFormat)





