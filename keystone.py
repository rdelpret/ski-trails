#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json

mountain_domain = "keystoneresort"
url = "https://www.%s.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx" % mountain_domain

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for script in soup.find_all('script'):
    if "FR.TerrainStatusFeed" in str(script):
        raw_conditions = str(script)
        break 


d = { 1 : "●", 2 : "■", 3 : "♦", 4 : "♦♦", 5 : "⬬"}

raw_conditions = raw_conditions.replace("<script>", "")
raw_conditions = raw_conditions.replace("</script>", "")
raw_conditions = raw_conditions.replace("\n", "")
raw_conditions = "{" + raw_conditions.split("{", 2)[2]
raw_conditions = raw_conditions.split(";")[0]
t = json.loads(raw_conditions)

for i in t["GroomingAreas"]:
    if "All Summer Terrain" in i["Name"]:
      continue
    print("-------------- " + i["Name"] + " ----------------")
    for t in i["Trails"]:
        o = "OPEN" if t["IsOpen"] else "CLOSED" 
        trail = "%-25s%-5s%s" % (t["Name"], d[t["Difficulty"]], o) 
        print(trail)
