from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import qconnect

def buryUnburyNSFW() -> None:
    if len(mw.col.find_cards("tag:buriedNSFW")):
        # Unbury cards
        ids = mw.col.find_cards("tag:buriedNSFW")
        mw.col.unbury_cards(ids, manual=True)
        mw.col.tags.bulk_remove(ids, 'buriedNSFW')
        showInfo(f"Unburied {len(ids)} cards")
    else:
        # Bury cards
        ids = mw.col.find_cards("tag:nsfw is:due")
        mw.col.tags.bulk_add(ids, 'buriedNSFW')
        mw.col.bury_cards(ids, manual=True)
        showInfo(f"Buried {len(ids)} cards")

def filterNSFW() -> None:
    pass

def unfilterNSFW() -> None:
    pass

button = QAction(f"{'B' if len(mw.col.find_cards("tag:buriedNSFW")) else 'Unb'}'ury NSFW cards", mw)
qconnect(button.triggered, buryUnburyNSFW)
mw.form.menuTools.addAction(button)