#!/usr/bin/python3

import sys
import os
import hashlib
import time
import json

# Add the following to /media/fat/downloader.ini
# [uberyoji_mister_boot_roms]
# db_url = https://raw.githubusercontent.com/uberyoji/mister-boot-roms/main/db/uberyoji_mister_boot_roms.json

tag = sys.argv[1]

db_name = "uberyoji_mister_boot_roms"

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
        return file_entry.format( pathname, hashlib.md5(open(fullname,'rb').read()).hexdigest(), os.path.getsize(fullname), "{}{}".format( db_url, filename ) )
    else:
        print( "{} not found".format(filename) )
        return ""

roms = [
    ("|games/Gameboy/boot2.rom","mister-boot.gb"),
    ("|games/Genesis/boot.rom","mister-boot.md"),
    ("|games/NES/boot1.rom","mister-boot.nes"),
    ("|games/SMS/boot.rom","mister-boot.sms"),
    ("|games/SNES/boot.rom","mister-boot.sfc"),
    ("|games/TGFX16/boot.rom","mister-boot.pce"),
    ("|games/S32X/boot.rom","mister-boot.32x"),
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
            "|games/NES/": {{ 
                "tags": []
            }},
            "|games/SNES/": {{ 
                "tags": []
            }},
            "|games/Genesis/": {{
                "tags": []
            }},
            "|games/SMS/": {{ 
                "tags": []   
            }},
            "|games/Gameboy/": {{ 
                "tags": []
            }},
            "|games/TGFX16/": {{ 
                "tags": []     
            }},
            "|games/S32X/": {{ 
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
