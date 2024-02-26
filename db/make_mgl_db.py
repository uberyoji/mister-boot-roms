#!/usr/bin/python3

import sys
import os
import hashlib
import time
import json

# Add the following to /media/fat/downloader.ini
# [uberyoji_mister_boot_roms]
# db_url = https://raw.githubusercontent.com/uberyoji/mister-boot-roms/main/db/uberyoji_mister_boot_roms_mgl.json

tag = sys.argv[1]

db_name = "uberyoji_mister_boot_roms_mgl"

if len(sys.argv) > 2:
    db_filename = sys.argv[2]+".json"
else:
    db_filename = db_name+".json"

db_url= "https://github.com/uberyoji/mister-boot-roms/releases/download/{}/".format(tag)

def get_file_props( entry ):
    pathname = entry[0]
    filename = entry[1]
    fullname = entry[1] # "../Games/{}".format(entry[1])

    if os.path.isfile(fullname):
        file_entry ="""
            "{0}": {{
                "hash": "{1}",
                "size": {2},
                "url": "{3}",
                "tags": [],
                "overwrite": true,
                "reboot": false
            }}"""
        return file_entry.format( pathname, hashlib.md5(open(fullname,'rb').read()).hexdigest(), os.path.getsize(fullname), ("{}{}".format( db_url, filename )).replace( ' ', '.') )
    else:
        print( "{} not found".format(filename) )
        return ""

roms = [
    ("|games/GameBoy/mister-boot.gb","mister-boot.gb"),
    ("|games/MegaDrive/mister-boot.md","mister-boot.md"),
    ("|games/NES/mister-boot.nes","mister-boot.nes"),
    ("|games/SMS/mister-boot.sms","mister-boot.sms"),
    ("|games/SNES/mister-boot.sfc","mister-boot.sfc"),
    ("|games/TGFX16/mister-boot.pce","mister-boot.pce"),
    ("|games/S32X/mister-boot.32x","mister-boot.32x"),
    ("|games/GBA/mister-boot.gba","mister-boot.gba"),
    ("|games/PSX/mister-boot.chd","mister-boot.chd"),
    ("|games/N64/mister-boot.z64","mister-boot.z64"),
    ("_Console (autoboot)/NEC PC Engine.mgl","NEC PC Engine.mgl"),
    ("_Console (autoboot)/Nintendo Gameboy.mgl","Nintendo Gameboy.mgl"),
    ("_Console (autoboot)/Nintendo NES.mgl","Nintendo NES.mgl"),
    ("_Console (autoboot)/Nintendo SNES.mgl","Nintendo SNES.mgl"),
    ("_Console (autoboot)/SEGA 32X.mgl","SEGA 32X.mgl"),
    ("_Console (autoboot)/SEGA Genesis.mgl","SEGA Genesis.mgl"),
    ("_Console (autoboot)/SEGA Master System.mgl","SEGA Master System.mgl"),
    ("_Console (autoboot)/Nintendo GBA.mgl","Nintendo GBA.mgl"),
    ("_Console (autoboot)/Sony PlayStation.mgl","Sony PlayStation.mgl"),
    ("_Console (autoboot)/Nintendo 64.mgl","Nintendo 64.mgl")
]

def validate(text):
    try:
        json.loads(text)
        print('valid json')
        return True
    except ValueError as e:
        print('invalid json: %s' % e)
        return False # or: raise

def build_json( tag ):
    json = """
    {{    
        "db_id": "{0}",
        "timestamp": {1},
        "files": {{
            {2}
        }},

        "folders": {{
            "|games/Gameboy/": {{ 
                "tags": []
            }},
            "|games/NES/": {{ 
                "tags": []
            }},
             "|games/SNES/": {{ 
                "tags": []
            }},
             "|games/MegaDrive/": {{ 
                "tags": []
            }},
             "|games/SMS/": {{ 
                "tags": []
            }},
             "|games/S32X/": {{ 
                "tags": []
            }},
             "|games/TGFX16/": {{ 
                "tags": []
            }},
             "|games/GBA/": {{ 
                "tags": []
            }},
             "|games/PSX/": {{ 
                "tags": []
            }},
            "|games/N64/": {{ 
                "tags": []
            }},
            "_Console (autoboot)": {{ 
                "tags": []
            }}
        }},

        "base_files_url": "https://github.com/uberyoji/mister-boot-roms/releases/download/{3}/"
    }}
    """

    files = ""
    for r in roms:
        files += get_file_props(r)
        files += ",\n"
    
    files = files[:-2]  # trim last comma

    return json.format( db_name, int(time.time()), files, tag )

json_content = build_json(tag);
# print( json_content )

if validate(json_content):
    json_file = open(db_filename,"w",encoding="utf8")
    json_file.write(json_content)
    json_file.flush()
    json_file.close()
    print('Done')
else:
    print('Something went wrong.')
