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

```
➜ cat config.yaml
resorts:
- urlBase: keystoneresort
  name: Keystone
- urlBase: vail
  name: Vail
- urlBase: breckenridge
  name: Breckenridge
- urlBase: beavercreek
  name: Beaver Creek
```
