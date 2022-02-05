import os
from couleur import *
from extensions import *
from end import end_sequence
from tools  import command_tools

is_running = 1
count = 1
not_running = [0,3]

while is_running not in not_running:
	try:
		nom = input(input_cyan("Nom de fichier: "))
	except:
		nom = input(input_cyan("Nom de fichier: "))
	fichier = open(nom,"w")
	content = []
	i = 1
	cont = 1
	vert("=Debut=")
	while cont:
		ligne = input(f"\033[1;32m{i}\033[1;36m ")
		i += 1
		content += [ligne]
		cont = command_tools(ligne,content,i)
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
        
	

