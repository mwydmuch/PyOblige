#!/usr/bin/env python

from __future__ import print_function
import os
import sys
import subprocess
import random

oblige_version = "7.70"

oblige_frequency_vals = ["mixed", "none", "rare", "few", "less", "some", "more", "heaps"]
oblige_mon_quantity_vals = ["default", "none", "scarce", "few", "less", "some", "more", "heaps", "insane"]
oblige_wep_quantity_vals = ["default", "none", "scarce", "less", "plenty", "more", "heaps", "loveit"]

# First value is default one
oblige_options = {

    # General options
    "game": ["doom2", "doom"],
    "engine": ["zdoom", "gzdoom", "vizdoom"],
    "length": ["single", "few", "episode", "game"],
    "theme": ["original", "mostly_original", "epi", "mostly_epi", "bit_mixed", "jumble",
              "tech", "mostly_tech", "urban", "mostly_urban", "hell", "mostly_hell"],

    "size": ["micro", "tiny", "small", "regular", "large", "extreme", "epi", "prog", "mixed"],
    "outdoors": oblige_frequency_vals,
    "caves": oblige_frequency_vals,
    "liquids": oblige_frequency_vals,
    "hallways": oblige_frequency_vals,
    "teleporters": oblige_frequency_vals,
    "steepness": oblige_frequency_vals,

    "mons": ["scarce", "few", "less", "some", "more", "nuts", "mixed", "none"],
    "strength": ["weak", "easier", "normal", "harder", "tough", "crazy"],
    "ramp_up": ["slow", "medium", "fast", "episodic"],
    "bosses": ["none", "easier", "normal", "harder"],
    "traps": ["none"] + oblige_frequency_vals,
    "cages": ["none"] + oblige_frequency_vals,

    "health": ["none", "scarce", "less", "bit_less", "normal", "bit_more", "more", "heaps"],
    "ammo": ["none", "scarce", "less", "bit_less", "normal", "bit_more", "more", "heaps"],
    "weapons": ["none", "very_soon", "sooner", "normal", "later", "very_late"],
    "items": ["none", "rare", "less", "normal", "more", "heaps"],
    "secrets": oblige_frequency_vals,

    # Modules' options
    "doom_mon_control": [0, 1],
    # doom_mon_control module options
    "Spiderdemon": oblige_mon_quantity_vals,
    "caco": oblige_mon_quantity_vals,
    "gunner": oblige_mon_quantity_vals,
    "skull": oblige_mon_quantity_vals,
    "demon": oblige_mon_quantity_vals,
    "knight": oblige_mon_quantity_vals,
    "vile": oblige_mon_quantity_vals,
    "zombie": oblige_mon_quantity_vals,
    "Cyberdemon": oblige_mon_quantity_vals,
    "ss_nazi": oblige_mon_quantity_vals,
    "baron": oblige_mon_quantity_vals,
    "spectre": oblige_mon_quantity_vals,
    "arach": oblige_mon_quantity_vals,
    "mancubus": oblige_mon_quantity_vals,
    "revenant": oblige_mon_quantity_vals,
    "pain": oblige_mon_quantity_vals,
    "imp": oblige_mon_quantity_vals,
    "shooter": oblige_mon_quantity_vals,

    "doom_weapon_control": [0, 1],
    # doom_weapon_control module options
    "super": oblige_wep_quantity_vals,
    "chain": oblige_wep_quantity_vals,
    "launch": oblige_wep_quantity_vals,
    "bfg": oblige_wep_quantity_vals,
    "plasma": oblige_wep_quantity_vals,
    "shotty": oblige_wep_quantity_vals,

    "export_map": [0, 1],

    "misc": [1, 0],
    # misc module options
    "pistol_starts": ["yes", "no"],
    "alt_starts": ["no", "yes"],
    "big_rooms": oblige_frequency_vals,
    "parks": oblige_frequency_vals,
    "windows": oblige_frequency_vals,
    "symmetry": oblige_frequency_vals,
    "darkness": oblige_frequency_vals,
    "mon_variety": oblige_frequency_vals,
    "barrels": oblige_frequency_vals,
    "doors": oblige_frequency_vals,
    "keys": oblige_frequency_vals,
    "switches": oblige_frequency_vals,

    "music_swapper": [1, 0],

    "sky_generator": [1, 0],

    "small_spiderdemon": [0, 1],

    "stealth_mons": [0, 1],
    "stealth_mons_qty": ["normal", "less", "more"],

    "stealth_mon_control": [0, 1],
    # stealth_mon_control module options
    "stealth_demon": oblige_mon_quantity_vals,
    "stealth_baron": oblige_mon_quantity_vals,
    "stealth_zombie": oblige_mon_quantity_vals,
    "stealth_caco": oblige_mon_quantity_vals,
    "stealth_imp": oblige_mon_quantity_vals,
    "stealth_mancubus": oblige_mon_quantity_vals,
    "stealth_arach": oblige_mon_quantity_vals,
    "stealth_revenant": oblige_mon_quantity_vals,
    "stealth_shooter": oblige_mon_quantity_vals,
    "stealth_vile": oblige_mon_quantity_vals,
    "stealth_knight": oblige_mon_quantity_vals,
    "stealth_gunner": oblige_mon_quantity_vals,

    "zdoom_marines": [0, 1],
    "zdoom_marines_qty": ["plenty", "scarce", "heaps"],

    "zdoom_marine_control": [0, 1],
    # zdoom_marine_control module options
    "marine_bfg": oblige_mon_quantity_vals,
    "marine_chain": oblige_mon_quantity_vals,
    "marine_pistol": oblige_mon_quantity_vals,
    "marine_ssg": oblige_mon_quantity_vals,
    "marine_rail": oblige_mon_quantity_vals,
    "marine_berserk": oblige_mon_quantity_vals,
    "marine_plasma": oblige_mon_quantity_vals,
    "marine_rocket": oblige_mon_quantity_vals,
    "marine_fist": oblige_mon_quantity_vals,
    "marine_saw": oblige_mon_quantity_vals,
    "marine_shotty": oblige_mon_quantity_vals,
}

oblige_config_str = """-- CONFIG FILE : OBLIGE 7.70
-- OBLIGE Level Maker (C) 2006-2017 Andrew Apted
-- http://oblige.sourceforge.net/
-- Generated by PyOblige
-- https://github.com/mwydmuch/PyOblige

seed = {seed}

---- Game Settings ----

game = {game}
engine = {engine}
length = {length}
theme = {theme}

---- Architecture ----

size = {size}
outdoors = {outdoors}
caves = {caves}
liquids = {liquids}
hallways = {hallways}
teleporters = {teleporters}
steepness = {steepness}

---- Monsters ----

mons = {mons}
strength = {strength}
ramp_up = {ramp_up}
bosses = {bosses}
traps = {traps}
cages = {cages}

---- Pickups ----

health = {health}
ammo = {ammo}
weapons = {weapons}
items = {items}
secrets = {secrets}

---- Other Modules ----

@doom_mon_control = {doom_mon_control}
  Spiderdemon = {Spiderdemon}
  caco = {caco}
  gunner = {gunner}
  skull = {skull}
  demon = {demon}
  knight = {knight}
  vile = {vile}
  zombie = {zombie}
  Cyberdemon = {Cyberdemon}
  ss_nazi = {ss_nazi}
  baron = {baron}
  spectre = {spectre}
  arach = {arach}
  mancubus = {mancubus}
  revenant = {revenant}
  pain = {pain}
  imp = {imp}
  shooter = {shooter}

@doom_weapon_control = {doom_weapon_control}
  super = {super}
  chain = {chain}
  launch = {launch}
  bfg = {bfg}
  plasma = {plasma}
  shotty = {shotty}

@export_map = {export_map}

@misc = {misc}
  pistol_starts = {pistol_starts}
  alt_starts = {alt_starts}
  big_rooms = {big_rooms}
  parks = {parks}
  windows = {windows}
  symmetry = {symmetry}
  darkness = {darkness}
  mon_variety = {mon_variety}
  barrels = {barrels}
  doors = {doors}
  keys = {keys}
  switches = {switches}

@music_swapper = {music_swapper}

@sky_generator = {sky_generator}

@small_spiderdemon = {small_spiderdemon}

@stealth_mon_control = {stealth_mon_control}
  stealth_demon = {stealth_demon}
  stealth_baron = {stealth_baron}
  stealth_zombie = {stealth_zombie}
  stealth_caco = {stealth_caco}
  stealth_imp = {stealth_imp}
  stealth_mancubus = {stealth_mancubus}
  stealth_arach = {stealth_arach}
  stealth_revenant = {stealth_revenant}
  stealth_shooter = {stealth_shooter}
  stealth_vile = {stealth_vile}
  stealth_knight = {stealth_knight}
  stealth_gunner = {stealth_gunner}

@stealth_mons = {stealth_mons}
  qty = {stealth_mons_qty}

@zdoom_marine_control = {zdoom_marine_control}
  marine_bfg = {marine_bfg}
  marine_chain = {marine_chain}
  marine_pistol = {marine_pistol}
  marine_ssg = {marine_ssg}
  marine_rail = {marine_rail}
  marine_berserk = {marine_berserk}
  marine_plasma = {marine_plasma}
  marine_rocket = {marine_rocket}
  marine_fist = {marine_fist}
  marine_saw = {marine_saw}
  marine_shotty = {marine_shotty}

@zdoom_marines = {zdoom_marines}
  qty = {zdoom_marines_qty}

-- END --
"""


def oblige_unique_vals(vals):
    seen = set()
    return [x for x in vals if not (x in seen or seen.add(x))]


def oblige_realpath(local_path):
    return os.path.realpath(os.path.realpath(os.path.join(os.path.dirname(__file__), local_path)))


class DoomLevelGenerator(object):
    def __init__(self, seed=None):
        if seed is not None:
            self.seed = seed
        else:
            self.seed = random.randint(0, 2147483647)
        self.config = {}
        for (k, v) in oblige_options.items():
            self.config[k] = v[0]

    def set_seed(self, seed):
        self.seed = seed

    def get_seed(self):
        return self.seed

    def set_config(self, new_config):
        for (k, v) in new_config.items():

            # Check if provided config is correct
            if k not in oblige_options:
                raise ValueError("Provided key {} is not valid Oblige option!".format(k))

            if v not in oblige_options[k]:
                raise ValueError("Provided value {} is not valid value of {}!\nAvailable values: "
                                 .format(v, k, oblige_unique_vals(oblige_options[k])))

            self.config[k] = v

    def generate(self, wad_path, verbose=False):
        # Config preprocessing
        if self.config["engine"] == "vizdoom":
            self.config["engine"] = "zdoom"

        if verbose:
            print("Config:")
            for (k, v) in self.config.items():
                if v != oblige_options[k][0]:
                    print("  {}: {}".format(k, v))

        # Prepare paths
        if os.path.isdir(wad_path):
            raise ValueError("{} is a directory!".format(wad_path))

        if os.path.splitext(wad_path)[1] != ".wad":
            wad_path += ".wad"

        wad_path = os.path.realpath(wad_path)
        config_path = os.path.realpath(os.path.splitext(wad_path)[0] + ".txt")

        with open(config_path, "w") as config_file:
            config_file.write(oblige_config_str.format(seed=self.seed, **self.config))

        if sys.platform in ["win32", "win64"]:
            oblige_exe = "Oblige.exe"
            oblige_path = "Oblige_src\\" + oblige_exe
        else:
            oblige_exe = "./Oblige"
            oblige_path = "Oblige_src/Oblige"

        oblige_dir = "Oblige_src"

        if not os.path.exists(oblige_realpath(oblige_path)):
            raise Exception("Oblige does not exists! Package is incomplete!")

        if verbose:
            print("Config text file path: {}"
                  "\nOutput wad file path: {}"
                  "\nOblige executable path: {}".format(config_path, wad_path, oblige_path))

        cmd = "{} --batch {} --load {} --keep".format(oblige_exe, wad_path, config_path)
        if verbose:
           cmd += " --verbose"

        # Launch Oblige
        try:
            oblige_process = subprocess.Popen(cmd, cwd=oblige_realpath(oblige_dir), shell=True,
                                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            results = oblige_process.communicate()[0]
            exit_code = oblige_process.returncode

        except subprocess.CalledProcessError:
            raise Exception("Oblige failed to generate .wad file!\nExit code: {}\nLog:\n{}"
                            .format(exit_code, results))

        if verbose:
            print("Exit code: {}\n"
                  "Oblige output:\n{}".format(exit_code, results))

        # Parse results
        maps = 1
        map_str = "MAP{:02}".format(maps)
        while str(results).find(map_str) != -1:
            maps += 1
            map_str = "MAP{:02}".format(maps)

        return maps - 1
