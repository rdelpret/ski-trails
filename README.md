# 🌲 ski-trails 🌲

Parses and displays data on ski trails from various sources. These sources are written as "plugins". 

Currently we have plugins for:
- Vail Resorts
- Arapahoe Basin 


## CLI Usage

Get all open trails
```
➜ ./trails --open

  RESORT         AREA                TRAIL                 DIFFICULTY  STATUS

  Keystone       Dercum Mountain     Endeavor              ●           OPEN
  Keystone       Dercum Mountain     Schoolmarm            ●           OPEN
  Arapaho Basin  Front Side Terrain  Lower Mountain Blues  ■           OPEN
  Arapaho Basin  Front Side Terrain  High Noon             ■           OPEN


```
Get all trails in Blue Sky Basin and sort by difficulty
```
➜ trails --sort difficulty --filter area=blue

  RESORT  AREA            TRAIL                 DIFFICULTY  STATUS

  Vail    Blue Sky Basin  Big Rock Park - East  ■           CLOSED
  Vail    Blue Sky Basin  Big Rock Park - West  ■           CLOSED
  Vail    Blue Sky Basin  China Spur            ■           CLOSED
  Vail    Blue Sky Basin  Cloud 9 - Lower       ■           CLOSED
  Vail    Blue Sky Basin  Cloud 9 - Middle      ■           CLOSED
  Vail    Blue Sky Basin  Cloud 9 - Upper       ■           CLOSED
  Vail    Blue Sky Basin  Grand Review          ■           CLOSED
  Vail    Blue Sky Basin  Grand Review - Lower  ■           CLOSED
  Vail    Blue Sky Basin  In The Wuides         ■           CLOSED
  Vail    Blue Sky Basin  Kelly's Toll Road     ■           CLOSED
  Vail    Blue Sky Basin  The Star              ■           CLOSED
  Vail    Blue Sky Basin  The Star - Lower      ■           CLOSED
  Vail    Blue Sky Basin  Encore                ♦           CLOSED
  Vail    Blue Sky Basin  Heavy Metal           ♦           CLOSED
  Vail    Blue Sky Basin  Hornsilver            ♦           CLOSED
  Vail    Blue Sky Basin  Iron Mask             ♦           CLOSED
  Vail    Blue Sky Basin  Little Ollie          ♦           CLOSED
  Vail    Blue Sky Basin  Lovers Leap           ♦           CLOSED
  Vail    Blue Sky Basin  Resolution            ♦           CLOSED
  Vail    Blue Sky Basin  Resolution Road       ♦           CLOSED
  Vail    Blue Sky Basin  Skree Field           ♦           CLOSED
  Vail    Blue Sky Basin  The Divide            ♦           CLOSED
  Vail    Blue Sky Basin  The Divide Ridge      ♦           CLOSED
  Vail    Blue Sky Basin  Steep and Deep        ♦♦          CLOSED
```


## Help
```
➜ ./trails --help
usage: trails [-h] [-o] [-s SORT] [-f FILTER]

Get Ski Trail Status

optional arguments:
  -h, --help            show this help message and exit
  -o, --open            Open trails only
  -s SORT, --sort SORT  sort by (--sort difficulty)
  -f FILTER, --filter FILTER
                        filter by (--filter difficulty=blue)

By default, show all trails from config.yaml
```

## Config
The configuration file adds or removes resorts you want to get trail info for. Currently the vail plugin can support any vail resort (you could add Park City for example as they are owned by vail) and the abasin plugin adds Arapahoe Basin trails.

```
➜ cat config.yaml
resorts:
- name: Keystone
  urlBase: keystoneresort.com
  plugin: vail
- name: Vail
  urlBase: vail.com
  plugin: vail
- name: Breckenridge
  urlBase: breckenridge.com
  plugin: vail
- name: Beaver Creek
  urlBase: beavercreek.com
  plugin: vail
- name: Arapahoe Basin
  urlBase: arapahoebasin.com
  plugin: abasin
```
