""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

# create GET request

def get_data_from_api():
    
    url = "https://fifa-2022-schedule-and-stats.p.rapidapi.com/schedule"
    params = {"date":"2022-11-22","utc_offset":"8"}
    headers = {
	"X-RapidAPI-Key": "8e6f634c5cmshf210e3a623f7435p1e10d5jsnd5433a37d688",
	"X-RapidAPI-Host": "fifa-2022-schedule-and-stats.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=params)
    outputs = response.json()

    return outputs
