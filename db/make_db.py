#!/usr/bin/python3

import sys
import os
import hashlib
import time
import json

# https://raw.githubusercontent.com/uberyoji/mister-boot-roms/main/db/uberyoji-mister-boot-roms.json
# https://github.com/uberyoji/mister-boot-roms/releases/download/

db_filename = "uberyoji-mister-boot-roms.json"

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
        return file_entry.format( pathname, hashlib.md5(open(fullname,'rb').read()).hexdigest(), os.path.getsize(fullname), filename )
    else:
        print( "{} not found".format(filename) )
        return ""

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

roms = [
    ("Games/Gameboy/boot2.rom","mister-boot.gb"),
    ("Games/Genesis/boot.rom","mister-boot.md"),
    ("Games/NES/boot1.rom","mister-boot.nes"),
    ("Games/SMS/boot.rom","mister-boot.sms"),
    ("Games/SNES/boot.rom","mister-boot.sfc"),
    ("Games/TGFX16/boot.rom","mister-boot.pce")
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
            "Games/NES/": {{ 
                "tags": []
            }},
            "Games/SNES/": {{ 
                "tags": []
            }},
            "Games/Genesis/": {{
                "tags": []
            }},
            "Games/SMS/": {{ 
                "tags": []   
            }},
            "Games/Gameboy/": {{ 
                "tags": []
            }},
            "Games/TGFX16/": {{ 
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

    return json.format( db_filename, int(time.time()), files, tag )

tag = sys.argv[1]

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
