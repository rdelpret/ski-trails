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

ratings = { "beginner" : 2, "moredifficult" : 2, "mostdifficult" : 3, "extreme" : 4,}

def get_trails():
  with open("data/abasin.json", "r") as f:
    trails = json.loads(f.read())
  return trails


def init_trails():
    rev_map = get_trails()
    trails = {"resort" : "Arapaho Basin", "areas" : []}
    areas = list(rev_map.values())
    areas = [i for n, i in enumerate(areas) if i not in areas[:n]]
    for i in areas:
        trails["areas"].append({"name" : i, "trails"  : []})
    return trails
 


def parse_trails(resort):

    trails = init_trails()

    url = "https://www.%s/the-mountain/terrain-status/" % resort["urlBase"]

    rev_map = get_trails()

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup = soup.find_all("div", {"class" : "ab-status"})
    
    for i in soup:
        name = i.text.strip()
        area = rev_map.get(name)
        try:
            level = str(i).split("level_")[1].split("\"")[0]
            status = str(i).split("status_")[1].split("\"")[0]
            status = status.upper()
        except:
            level = False
            status = False
        if level and area:
            trail  = {"name" : name, "status" : status, "rating" : ratings[level]}
            area_index = 0
            for a in trails["areas"]:
                if rev_map.get(name) == a["name"]:
                    break 
                area_index += 1
            trails["areas"][area_index]["trails"].append(trail)
    return trails

def main():
    pass

if __name__ == "__main__":
    main()
