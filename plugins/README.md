# Plugins

## Adding a plugin
#### The name of the plugin needs to match the <plugin>.py file in the plugins dir
```
abasin.py -> abasin
vail.py -> vail
```
#### Plugin function name needs to match the name of the plugin and takes in a resort from the config file
```
def abasin(resort):
```
For example:
```
resort = {"name": "Arapahoe Basin", "urlBase": "arapahoebasin.com", "plugin": "abasin"}
```
#### Plugin function will output the following data structure
```
trails = {"resort" : "", "areas" : [{"name" : "", "trails" : [{"name" : "", "status" : "", "rating" : ""},]},]}

trails = {"resort" : "", "areas" : []}
area   = {"name" : "", "trails" : []}
trail  = {"name" : "", "status" : "", "rating" : ""}
```
#### Helper data
Since vail was written first, that is where the data structure is from. For abasin I dumped a map into a file called `data/abasin.json` to help map trails to areas as this was not easilly done dynamically
You may want to follow this pattern if it is not easy to map a trail to an area. At some point it may make sense to rethink this.

#### "installing" your plugin"
import your plugin in trails like so and if you followed all the directions and contracts above it should just work
```
# Plugins
from plugins.vail import vail
from plugins.abasin import abasin
```
#### using the plugin
call your plugin in the config file:
```
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
