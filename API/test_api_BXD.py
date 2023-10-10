#!/bin/python 

import requests 

api_url = "https://genenetwork.org/api/v_pre1/genotypes/bimbam/BXD"
response = requests.get(api_url)

if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Response content is not valid JSON")
else:
    print("Request failed with status code:", response.status_code)
