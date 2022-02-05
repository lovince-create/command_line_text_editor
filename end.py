from couleur import *
from extensions import run_by_extension
def display_interface(count,nom):
        filenom = nom.split(".")
        fichier = open(nom,"r")
        vert(f"=Fichier \"{nom}\"=")
        for i in fichier.readlines():
            print(f"\033[1;36m{count}\033[1;32m {i}",end="")
            count += 1
        jaune("\n==Execution==")
        print(run_by_extension(nom,filenom[-1]))
        
def end_sequence(switch,count,nom):
    fichier = open(nom,"r")
    if switch == 0:
        cyan(f"=Fichier \"{nom}\"=")
        for i in fichier.readlines():
            print(f"\033[1;36m{count}\033[1;32m {i}",end="")
            count += 1
    if switch == 1:
        cyan(f"=Fichier \"{nom}\"=")
        for i in fichier.readlines():
            print(f"\033[1;36m{count}\033[1;32m {i}",end="")
            count += 1
        vert("==Nouveau==")
    if switch == 2:
        display_interface(count,nom)
        cyan("==Nouveau==")
    if switch == 3:
        display_interface(count,nom)
