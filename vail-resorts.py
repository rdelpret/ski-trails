#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import yaml
from columnar import columnar
from click import style
import sys

'''
Data Structure
trails = {"resort" : "", "areas" : []}
area   = {"name" : "", "trails" : []}
trail  = {"name" : "", "status" : "", "rating" : ""}
'''


def parse_trails(mountain_domain, name, open):
    url = "https://www.%s.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx" % mountain_domain

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

    trails = {"resort" : name, "areas" : []}

    for a in t["GroomingAreas"]:

        if "All Summer Terrain" in a["Name"]:
          continue

        area   = {"name" : a["Name"], "trails" : []}

        for t in a["Trails"]:
            if not t["IsOpen"]:
                continue
            trail  = {"name" : t["Name"], "rating" : t["Difficulty"]}
            trail["status"] = "OPEN" if t["IsOpen"] else "CLOSED"
            area["trails"].append(trail)
        trails["areas"].append(area)
    return trails 

def get_config():
  with open("config.yaml", "r") as f:
    config = yaml.load(f.read(), Loader=yaml.SafeLoader)
  return config

def main():
    if len(sys.argv) > 1  and sys.argv[1] == "open":
      open = True
    ratings = { 1 : "●", 2 : "■", 3 : "♦", 4 : "♦♦", 5 : "⬬"}
    resorts = get_config()["resorts"]

    data = []
    for resort in resorts:
        t = parse_trails(resort["urlBase"], resort["name"], open)
                
        for a in t["areas"]:
            for r in a["trails"]:
                trail = [t["resort"], a["name"], r["name"], ratings[r["rating"]], r["status"]]
                data.append(trail) 

    patterns = [
        ('OPEN', lambda text: style(text, fg='green')),
        ('●', lambda text: style(text, fg='green')),
        ('■', lambda text: style(text, fg='blue')),
        ('⬬', lambda text: style(text, fg='red')),
    ]   


    table = columnar(data, headers=['Resort', 'Area', 'Trail', 'Difficulty', 'Status'], patterns=patterns, no_borders=True)
    print(table)    

if __name__ == "__main__":
    main()
