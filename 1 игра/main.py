
# 🔥 🌲 🌊 ❤️ 🏠 🏦 🌁 ⚡ 🚁 ⬜ 🍚 🏆 ⬛

from clouds import Clouds
from map import Map
import time

import json



TICK_SLEEP =0.05
TREE_UPDATE=50
CLOUDS_UPDATE=30
FARE_UPDATE=75
MAP_W,MAP_H =20,10


tmp= Map (MAP_W,MAP_H)
clouds= Clouds(MAP_W,MAP_H)

tick=1


MOVES ={'w':(-1,0),'d':(0,1),'s':(1,0),'a':(0,-1)}

def process_key(key):
    global helico,tice,clouds,tmp
    c=key.char.lower()

    if c in MOVES.keys():
        dx,dy=MOVES[c][0],MOVES[c][1]
        helico.move(dx,dy)
    elif c == 'f':
        data={"helicopter": helico.export_data(),
              "clouds": clouds.export_data(),
              "tmp": tmp.export_date(),
              "tick":tick}
        with open("livel.json","w") as lvl:
            json.dump(data,lvl)
    elif c =='g':
        with open("level.json","r") as lvl:
            data = json.load(lvl)
            tick=data["tick"] or 1
            helico.import_data(data["helicopter"])
            tmp.import_data(data["tmp"])
            clouds.import_data(data["clouds"])


while True:

    print("TICK",tick)
    tick+=1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE ==0):
        tmp.generate_tree()
    if (tick % FARE_UPDATE ==0):
        tmp.update_fires()
    if (tick % CLOUDS_UPDATE ==0):
        clouds.update()