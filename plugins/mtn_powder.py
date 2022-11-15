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


def mtn_powder(resort):
    print(resort)
    resort_id = resort["resort_id"]
    url = f"https://mtnpowder.com/feed?resortId={resort_id}"
    data = requests.get(url).json()

    trails = {"name" : resort["name"], "areas" : []}

    for ma in data['MountainAreas']:
        area = {
            "name": ma['Name'],
            "trails": [] 
        }

        for tr in ma['Trails']:
            trail = {
                "name": tr['Name'],
                # "rating": tr['Difficulty'],
                "rating": 'green',
                "status": tr['Status']
            }
            area['trails'].append(trail)

        trails['areas'].append(area)

        # print(area)

    # area = {"name": "Some Region", "trails": []}
    # trail = {"name": "Duncan's Run", "rating": "green", "status": "OPEN"}
    # area["trails"].append(trail)
    # trails["areas"].append(area)

    # for a in t["GroomingAreas"]:

    #     if "All Summer Terrain" in a["Name"]:
    #       continue

    #     area   = {"name" : a["Name"], "trails" : []}

    #     for t in a["Trails"]:
    #         trail  = {"name" : t["Name"], "rating" : t["Difficulty"]}
    #         trail["status"] = "OPEN" if t["IsOpen"] else "CLOSED"
    #         area["trails"].append(trail)
    #     trails["areas"].append(area)
    return trails 

def main():
    pass

if __name__ == "__main__":
    main()
