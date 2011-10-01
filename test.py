from pymongo import Connection
from mongofts import Mongofts
import pprint

conn = Connection()
coll = conn.fts.coll
coll.remove()

fts = Mongofts(coll)
fts.insert_text("fuck this shit",3)
pprint.pprint(fts.search_text_any("fuck oh yeah"))
pprint.pprint(fts.search_text_all("fuck oh yeah"))
pprint.pprint(fts.search_text_all("fuck shit"))
