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


def vail(resort):
    url = "https://www.%s/the-mountain/mountain-conditions/terrain-and-lift-status.aspx" % resort["urlBase"]

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for script in soup.find_all('script'):
        if "FR.TerrainStatusFeed" in str(script):
            raw_conditions = str(script)
            break 
    
    raw_conditions = raw_conditions.replace("<script>", "")
    raw_conditions = raw_conditions.replace("</script>", "")
    raw_conditions = raw_conditions.replace("\n", "")
    raw_conditions = "{" + raw_conditions.split("{", 2)[2]
    raw_conditions = raw_conditions.split(";")[0]
    t = json.loads(raw_conditions)

    trails = {"resort" : resort["name"], "areas" : []}

    for a in t["GroomingAreas"]:

        if "All Summer Terrain" in a["Name"]:
          continue

        area   = {"name" : a["Name"], "trails" : []}

        for t in a["Trails"]:
            trail  = {"name" : t["Name"], "rating" : t["Difficulty"]}
            trail["status"] = "OPEN" if t["IsOpen"] else "CLOSED"
            area["trails"].append(trail)
        trails["areas"].append(area)
    return trails 

def main():
    pass

if __name__ == "__main__":
    main()
