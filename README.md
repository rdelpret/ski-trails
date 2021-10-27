#🌲 ski-trails 🌲

One of the benifits of vail resports (lol) is they all use the same code for their webistes, so we can parse it.

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
