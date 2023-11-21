#!/usr/bin/env python3

import requests

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
  'extremely_difficult': 'double',
  'extremely_difficult_2' : 'double'
}

def cleanup_status(status):
    if status == "opening":
        return "OPEN"
    if status == "closed":
        return "CLOSED"
    return status

def copper_eldora(resort):
    url = "https://api.%s/api/v1/dor/status" % resort["urlBase"]
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
