""" This script store the function required to stream data from the API of your choice"""

import requests
import json
import pandas as pd
import numpy as np

# create GET request

def get_data_from_api():
    
    url = "https://fifa-2022-schedule-and-stats.p.rapidapi.com/schedule"
    headers = {
	"X-RapidAPI-Key": "0cfd521736mshbc628a58783b056p161784jsn878d4847805f",
	"X-RapidAPI-Host": "fifa-2022-schedule-and-stats.p.rapidapi.com"
}
    params = {"date":"2022-12-02","utc_offset":"8"}

    response = requests.get(url, headers=headers, params=params)
    outputs = response.json()

    return outputs