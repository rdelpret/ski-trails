#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import yaml
import os

'''
Data Structure
trails = {"resort" : "", "areas" : []}
area   = {"name" : "", "trails" : []}
trail  = {"name" : "", "status" : "", "rating" : ""}
'''

difficulty_map = {
    "icon_beginner": "green",
    "icon_more_difficult": "blue",
    "icon_most_difficult": "black",
    "icon_expert": "double",
}

def get_rating(td):
    img_alt = td.find('img')['alt'].strip()
    return difficulty_map[img_alt]

def open_or_closed(td):
    img_src = td.find('img')['src']
    # print(img_src)
    if "icon_open" in img_src: 
        return "OPEN"
    if "icon_closed" in img_src:
        return "CLOSED"
    return "UNKNOWN"

def loveland(resort):

    trails = { "resort": "Loveland", "areas": [] }

    url = "https://skiloveland.com/trail-lift-report/"

    # their nginx config requires a user-agent
    r = requests.get(url, headers = { "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"})
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Start the scrape from the header of each section
    soup = soup.find_all("h2", {"class": "tablepress-table-name"})
    for header_div in soup:
        lift_name = header_div.text.strip()
        lift_name = lift_name.split(' - ')[0].strip()
        area = { 
            "name": lift_name, 
            "trails": [] 
        }

        # parse the table under the header
        lift_table = header_div.find_next_sibling('table')
        rows = lift_table.find_all("tr")
        rows = rows[1::] # drop the header row
        for tr in rows:
            tds = list(tr.children)
            trail = {
                "name": tds[3].text.strip(),
                "rating": get_rating(tds[1]),
                "status": open_or_closed(tds[2])
            }
            area["trails"].append(trail)

        trails["areas"].append(area)

    return trails


def main():
    pass


if __name__ == "__main__":
    main()
