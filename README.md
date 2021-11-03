# 🌲 ski-trails 🌲

Parses and displays data on ski trails from various sources. These sources are written as "plugins". 

Currently we have plugins for:
- Vail Resorts
- Arapahoe Basin 


## Usage
```
➜ ./trails --open

  RESORT    AREA             TRAIL       DIFFICULTY  STATUS

  Keystone  Dercum Mountain  Endeavor    ●           OPEN
  Keystone  Dercum Mountain  Schoolmarm  ●           OPEN
```

## Help
```
./trails --help
usage: trails [-h] [-o]

Get Ski Trail Status

optional arguments:
  -h, --help  show this help message and exit
  -o, --open  Open trails only

By default, show all trails from config.yaml
```

## Config
The configuration file adds or removes resorts you want to get trail info for. Currently the vail plugin can support any vail resort (you could add Park City for example as they are owned by vail) and the abasin plugin adds Arapahoe Basin trails.

```
➜ cat config.yaml
- plugin: vail
  resorts:
  - name: Keystone
    urlBase: keystoneresort.com
  - name: Vail
    urlBase: vail.com
  - name: Breckenridge
    urlBase: breckenridge.com
  - name: Beaver Creek
    urlBase: beavercreek.com
- plugin: abasin
  resorts:
  - name: Arapahoe Basin
```
