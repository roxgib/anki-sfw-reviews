from aqt import mw
from aqt.utils import qconnect, tooltip
from aqt.qt import qconnect, QAction
from aqt import gui_hooks

from datetime import date
import json

ids_filename = '_ids.json'

def buryUnburyNSFW() -> None:
    try:
        with open(ids_filename, 'r') as f:
            ids = json.loads(f.read())
    except:
        ids = [0,'']

    if ids[0] != str(date.today()) or ids[1] == '':
        # Bury cards
        ids = mw.col.find_cards("tag:nsfw is:due")
        mw.col.sched.bury_cards(ids)
        tooltip(f"Buried {len(ids)} card{'' if len(ids) == 1 else 's'}.")
        
        with open(ids_filename, 'w') as f:
            f.write(json.dumps([str(date.today()),list(ids)]))

        if {len(ids)} != 0:
            menuItem.setText("Unbury NSFW Cards")

    else:
        # Unbury cards
        ids = ids[1]
        mw.col.sched.unbury_cards(ids)
        tooltip(f"Unburied {len(ids)} card{'' if len(ids) == 1 else 's'}.")
        
        with open(ids_filename, 'w') as f:
            f.write(json.dumps([str(date.today()),'']))

        menuItem.setText("Bury NSFW Cards")
    
    mw.reset()

def filterNSFW() -> None:
    pass

def unfilterNSFW() -> None:
    pass

def initialise() -> None:
    try:
        with open(ids_filename, 'r') as f:
            ids = json.loads(f.read())
    except:
        ids = [0,'']

    if ids[0] != str(date.today()) or ids[1] == '':
        menuItem.setText("Bury NSFW Cards")
    else:
        menuItem.setText("Unbury NSFW Cards")

    mw.reset()

menuItem = QAction(f"Bury NSFW Cards", mw)
qconnect(menuItem.triggered, buryUnburyNSFW)
mw.form.menuTools.addAction(menuItem)
gui_hooks.profile_did_open.append(initialise)