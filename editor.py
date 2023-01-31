#!/usr/bin/python3
import readline,os,sys
from couleur import *
from extensions import *
from end import end_sequence
from tools  import command_tools

content = []
nom = sys.argv[1] or input_cyan("Nom de fichier: ") 
def main():
    global content
    global nom
    is_running = 1
    count = 1
    not_running = [0,3]
    safety = []
    contexclusion = [2,3,4]
    i = 1
    while is_running not in not_running:
        if os.path.exists(nom):
            with open(nom,"r") as fichier:
                data = fichier.read()
                vert("=Debut=")
                if len(data) == 0: 
                    content = []
                else:
                    content = data.split("\n")
                    safety = data.split("\n")
                    i = len(content) + 1
                    for index,element in enumerate(content):
                        print(f"\033[1;32m{index+1}\033[1;36m {element}")
                    
        fichier = open(nom,"w")
        cont = 1
        try:
            while cont:
                ligne = input(f"\033[1;32m{i}\033[1;36m ")
                content += [ligne]
                cont = command_tools(nom,ligne,content,i)
                if cont not in contexclusion:
                    i += 1
                if cont == 3:
                    i -= 1
                if cont == 4:
                    i = len(content) + 1
        except KeyboardInterrupt:
            print("Vous avez utilisé le code KeyboardInterrupt, utilisez :q svp")
            
        fichier.write("\n".join(content))
        fichier.close()
        print("0\tQuitter\n"
              "1\tRelancer\n"
              "2\tExecuter et relancer\n"
              "3\tExecuter et quitter")
        try:
            is_running = int(input("> "))
        except ValueError:
            is_running = int(input("> "))
        os.system("clear")
        end_sequence(is_running,count,nom)

while 1:
    try:
        main()
    except ValueError:
        content.pop()
        open(nom,"w").write("\n".join(content))
        print("Erreur de commande. Activation de la sauvegarde... Pressez Enter pour relancer, entrez N pour quitter")
        key = input()
        if key == "N":
            break
        else:
            os.system("clear")
        

            
