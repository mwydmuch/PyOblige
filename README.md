# PyOblige

[OBLIGE](http://oblige.sourceforge.net) is a random level generator 
for the classic FPS game Doom by Andrew Apted and contributors.

This project wraps it into small python class.
The main aim is to make it easier to use with [ViZDoom](https://github.com/mwydmuch/ViZDoom) project.
It also adds 2 additional level sizes: `micro` and `tiny`. 

## Install
```
pip install oblige
```

or install the newest version from the repository:

```
pip install git+https://github.com/mwydmuch/PyOblige
```

## Usage

### Example

PyOblige is really simple to use:

```
from oblige import *

generator = DoomLevelGenerator(seed)
generator.set_seed(another_seed)
generator.set_config({"key_to_update": "value"})
number_of_generate_maps = generator.generate("name_of_wad_file")
```

Example of usage with ViZDoom: [ViZDoom/examples/python/oblige.py](https://github.com/mwydmuch/ViZDoom/examples/python/oblige).


### Options
\<key>: \<possible values> (first value is default one)

#### General options

- `"game"`: `"doom2"`, `"doom"`
- `"engine"`: `"zdoom"`, `"gzdoom"`, `"vizdoom"`
- `"length"`: `"single"`, `"few"`, `"episode"`, `"game"`
- `"theme"`: `"original"`, `"mostly_original"`, `"epi"`, `"mostly_epi"`, `"bit_mixed"`, `"jumble"`
          `"tech"`, `"mostly_tech"`, `"urban"`, `"mostly_urban"`, `"hell"`, `"mostly_hell"`

- `"size"`: `"micro"`, `"tiny"`, `"small"`, `"regular"`, `"large"`, `"extreme"`, `"epi"`, `"prog"`, `"mixed"`
- `"outdoors"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"caves"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"liquids"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"hallways"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"teleporters"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"steepness"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`

- `"mons"`: `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"nuts"`, `"mixed"`, `"none"`
- `"strength"`: `"weak"`, `"easier"`, `"normal"`, `"harder"`, `"tough"`, `"crazy"`
- `"ramp_up"`: `"slow"`, `"medium"`, `"fast"`, `"episodic"`
- `"bosses"`: `"none"`, `"easier"`, `"normal"`, `"harder"`
- `"traps"`: `"none"`, `"mixed"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"cages"`: `"none"`, `"mixed"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`

- `"health"`: `"none"`, `"scarce"`, `"less"`, `"bit_less"`, `"normal"`, `"bit_more"`, `"more"`, `"heaps"`
- `"ammo"`: `"none"`, `"scarce"`, `"less"`, `"bit_less"`, `"normal"`, `"bit_more"`, `"more"`, `"heaps"`
- `"weapons"`: `"none"`, `"very_soon"`, `"sooner"`, `"normal"`, `"later"`, `"very_late"`
- `"items"`: `"none"`, `"rare"`, `"less"`, `"normal"`, `"more"`, `"heaps"`
- `"secrets"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`

#### Modules' options

##### misc module options
- `"misc"`: `1`, `0`
- `"pistol_starts"`: `"yes"`, `"no"`
- `"alt_starts"`: `"no"`, `"yes"`
- `"big_rooms"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"parks"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"windows"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"symmetry"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"darkness"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"mon_variety"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"barrels"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"doors"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"keys"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`
- `"switches"`: `"mixed"`, `"none"`, `"rare"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`

##### doom_mon_control module options
- `"doom_mon_control"`:`0`, `1`
- `"Spiderdemon"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"caco"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"gunner"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"skull"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"demon"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"knight"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"vile"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"zombie"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"Cyberdemon"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"ss_nazi"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"baron"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"spectre"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"arach"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"mancubus"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"revenant"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"pain"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"imp"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"shooter"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`

##### doom_weapon_control module options
- `"doom_weapon_control"`: `0`, `1`
- `"super"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`
- `"chain"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`
- `"launch"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`
- `"bfg"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`
- `"plasma"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`
- `"shotty"`: `"default"`, `"none"`, `"scarce"`, `"less"`, `"plenty"`, `"more"`, `"heaps"`, `"loveit"`

##### export_map module options
- `"export_map"`: `0`, `1`

##### export_map module options
- `"music_swapper"`: `1`, `0`

##### export_map module options
- `"sky_generator"`: `1`, `0`

##### export_map module options
- `"small_spiderdemon"`: `0`, `1`

##### export_map module options
- `"stealth_mons"`: `0`, `1`
- `"stealth_mons_qty"`: `"normal"`, `"less"`, `"more"`

##### stealth_mon_control module options
- `"stealth_mon_control"`: `0`, `1`
- `"stealth_demon"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_baron"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_zombie"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_caco"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_imp"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_mancubus"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_arach"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_revenant"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_shooter"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_vile"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_knight"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"stealth_gunner"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`

##### zdoom_marines module options
- `"zdoom_marines"`: `0`, `1`
- `"zdoom_marines_qty"`: `"plenty"`, `"scarce"`, `"heaps"`

##### zdoom_marine_control module options
- `"zdoom_marine_control"`: `0`, `1`
- `"marine_bfg"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_chain"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_pistol"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_ssg"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_rail"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_berserk"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_plasma"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_rocket"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_fist"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_saw"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`
- `"marine_shotty"`: `"default"`, `"none"`, `"scarce"`, `"few"`, `"less"`, `"some"`, `"more"`, `"heaps"`, `"insane"`


## Original OBLIGE's info

- [README.txt](https://github.com/mwydmuch/PyOblige/README.txt)
- [AUTHORS.txt](https://github.com/mwydmuch/PyOblige/AUTHORS.txt)
- [CHANGES.txt](https://github.com/mwydmuch/PyOblige/CHANGES.txt)
- [INSTALL.txt](https://github.com/mwydmuch/PyOblige/INSTALL.txt)

## License

OBLIGE and PyOblige are free software, distributed under the terms 
of the [GNU General Public License](https://github.com/mwydmuch/PyOblige/GPL.txt)

