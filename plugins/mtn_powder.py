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
  'GreenCircle': 'green',
  'Park': 'park',
  'BlackDiamond': 'black',
  'BlueBlackSquare': 'black', # TODO: Blue black?
  'BlueSquare': 'blue',
  'ExtremeTerrain': 'double',
  'DoubleBlackDiamond': 'double'
}

def mtn_powder(resort):
    resort_id = resort["mtn_powder_resort_id"]
    url = f"https://mtnpowder.com/feed?resortId={resort_id}"
    data = requests.get(url).json()

    trails = {"name" : resort["name"], "areas" : []}

    for ma in data['MountainAreas']:
        area = {
            "name": ma['Name'],
            "trails": [] 
        }

        for tr in ma['Trails']:
            
            # Steamboat has their snowshoe trails listed
            if tr['TrailIcon'] == 'Snowshoe':
                continue

            trail = {
                "name": tr['Name'],
                "rating": difficulty_map[tr['TrailIcon']],
                "status": tr['Status']
            }
            area['trails'].append(trail)

        trails['areas'].append(area)

    return trails 

def main():
    pass

if __name__ == "__main__":
    main()
