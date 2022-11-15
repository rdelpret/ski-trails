#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import yaml

'''
Data Structure
trails = {"resort" : "", "areas" : []}
area   = {"name" : "", "trails" : []}
trail  = {"name" : "", "status" : "", "rating" : ""}
'''

difficulty_map =  {
  'easier': 'green',
  'more_difficult': 'blue',
  'most_difficult': 'black',
  'extremely_difficult': 'double'
}

def cleanup_status(status):
    if status == "opening":
        return "Open"
    if status == "closed":
        return "Closed"
    return status

def copper(resort):
    url = "https://www.coppercolorado.com/api/v1/dor/status"
    data = requests.get(url).json()
    data = list(filter(lambda d: d["subtype"] == "alpine trail", data))

    trails = {"name" : resort["name"], "areas" : []}

    # pull the areas out of the data
    area_lookup = {}
    for area_name in set(map(lambda x: x['sector'], data)):
        area = {
            "name": area_name,
            "trails": []
        }
        area_lookup[area_name] = area
        trails["areas"].append(area)

    for tr in data:
        trail = {
            "name": tr["properties"]["name"],
            "rating": difficulty_map[tr["properties"]["subtype"]],
            "status": cleanup_status(tr["properties"]["global_status"])
        }
        area_name = tr["sector"]
        area_lookup[area_name]["trails"].append(trail)

    return trails 

def main():
    pass

if __name__ == "__main__":
    main()
