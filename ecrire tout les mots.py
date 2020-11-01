################################################################################

#Copyright Enzo ROUSSEL, All right reserved.

################################################################################
import pygame
from pygame.locals import *
import requests
from bs4 import BeautifulSoup

def printBlit(screen, string, coor="middle", taille=50, color=(255,255,255)):
    if coor == "middle":
        text = pygame.font.SysFont("arial", taille).render(string, 1, color)
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2 - text.get_height()//2))
    elif coor == "j":
        text = pygame.font.SysFont("arial", taille).render(string, 1, color)
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2 - text.get_height()//2 + 50))
        
    else:
        screen.blit(pygame.font.SysFont("arial", taille).render(string, 1, color), coor)

def get_def(word):
    try:
        soup = BeautifulSoup(requests.get(f"https://fr.wiktionary.org/wiki/{word}").text, "html.parser")
        for defs in soup.find_all("ol"):
            return defs.text
            break
    except:
        return "pas de définition trouvé."

class mot:
    def __init__(self, name):
        self.current = 0
        self.name = name

    def charger(self):
        with open(self.name+".txt", "r") as f:
            for ligne in f:
                self.current = int(ligne.strip("\n"))
                break

    def sauvegarder(self):
        with open(self.name+".txt", "w") as f:
            f.write(str(self.current))

    def add_one(self):
        self.current += 1

    def get_current(self):
        return self.current
        
pygame.init()
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)

f = open("mot.txt", "r", encoding="utf-8")
mots = f.read().split("\n")
print(mots[:500])

pSave = mot("ps1")
pSave.charger()

output = ""

motCurrent = mots[pSave.current]
definition = get_def(motCurrent)

done = True
while done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == 113:
                output += "a"
            if event.key == 119:
                output += "z"
            if event.key == 101:
                output += "e"
            if event.key == 114:
                output += "r"
            if event.key == 116:
                output += "t"
            if event.key == 121:
                output += "y"
            if event.key == 117:
                output += "u"
            if event.key == 105:
                output += "i"
            if event.key == 111:
                output += "o"
            if event.key == 112:
                output += "p"
            if event.key == 97:
                output += "q"
            if event.key == 115:
                output += "s"
            if event.key == 100:
                output += "d"
            if event.key == 102:
                output += "f"
            if event.key == 103:
                output += "g"
            if event.key == 104:
                output += "h"
            if event.key == 106:
                output += "j"
            if event.key == 107:
                output += "k"
            if event.key == 108:
                output += "l"
            if event.key == 59:
                output += "m"
            if event.key == 122:
                output += "w"
            if event.key == 120:
                output += "x"
            if event.key == 99:
                output += "c"
            if event.key == 118:
                output += "v"
            if event.key == 98:
                output += "b"
            if event.key == 110:
                output += "n"
            if event.key == 44:
                output += "."
            if event.key == 257:
                output += "1"
            if event.key == 258:
                output += "2"
            if event.key == 259:
                output += "3"
            if event.key == 260:
                output += "4"
            if event.key == 261:
                output += "5"
            if event.key == 262:
                output += "6"
            if event.key == 263:
                output += "7"
            if event.key == 264:
                output += "8"
            if event.key == 265:
                output += "9"
            if event.key == 256:
                output += "0"
            if event.key == 50:
                output += "é"
            if event.key == 52:
                output += "'"
            if event.key == 54:
                output += "-"
            if event.key == 55:
                output += "è"
            if event.key == 48:
                output += "à"
            if event.key == 93:
                output += "$"
            if event.key == K_BACKSPACE:
                output = output[:-1]
            if event.key == K_SPACE:
                output += " "
            if event.key == K_ESCAPE:
                pSave.sauvegarder()
                
            if output == motCurrent:
                pSave.add_one()
                motCurrent = mots[pSave.current]
                definition = get_def(motCurrent)
                pSave.sauvegarder()
                output = ""
                
    printBlit(screen, f"mot: {motCurrent}")
    if output == motCurrent[:len(output)]:
        color = (0,200,0)
    else:
        color = (200,0,0)
    printBlit(screen, f"Joueur: {output}", "j", color=color)
    try:
        for i, ligne in enumerate(definition.split("\n")):
            if i*15 > 490:
                printBlit(screen, ligne, (0, 130+i*15), 15)
            else:
                printBlit(screen, ligne, (0, i*15), 15)
                
    except:
        pass

    pygame.display.flip()
