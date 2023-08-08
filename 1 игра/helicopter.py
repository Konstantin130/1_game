from msilib.schema import SelfReg
from typing import Self
from utils import randcell
import os

class Helicopter:
    def __init__(self,w,h):
        rc=randcell(w,h)
        rx,ry =rc[0],rc[1]
        self.x=rx
        self.y=ry
        self.w=w
        self.h=h
        self.tank=0
        self.mxtaank=1
        self.score=0
        self.lives =20

    def move(self,dx,dy):
        nx,ny=dx + self.x,dy+self.y
        if (nx >=0 and ny >=0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print("🍚 ",self.tank, "/", self.mxtaank,sep="",end=" | ")
        print("🏆", self.score, end=" | ")
        print("❤️",self.lives)

    def game_over(self):
        os.system("clear")
        print("GAME OVER,YOUR SCORE IS",self.score)
        exit(0)

    def export_data(selt):
        return{"score": Self.score,
               "lives": Self.lives,
               "x": Self.x,  
               "y": Self.y,"tank": Self.tank,
               "mxtank":Self.mxtank}
    
    def import_date(self,data):
        self.x=data["x"] or 0
        self.y=data["y"] or 0
        self.tank=data["tank"] or 0
        self.mxtank=data["mxtank"] or 1
        self.lives=data["lives"] or 3
        self.score=data["score"] or 0
