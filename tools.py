import re
from couleur import *
from os import system

output = ""
def replace(line,ligne,content):
    line_index = int(line[-1]) - 1
    temp = content[line_index]
    cyan("--Remplacement--")
    cyan(f"old> {content[line_index]}")
    replacement = input(input_cyan("new> "))
    replacement = replacement.replace("\%",temp)
    content[line_index] = replacement
    cyan("::Remplacement effectue::")
    content.remove(ligne)
        
def copy(line,ligne,content):
    first_index = int(line[0]) - 1
    last_index = int(line[-1]) - 1
    content[last_index]  = content[first_index]
    content.remove(ligne)
    cyan("--Copie effectuee--")
        
def swap(line,ligne,content):
    first_index = int(line[0]) - 1
    last_index = int(line[-1]) - 1
    content[first_index], content[last_index] = content[last_index],content[first_index]
    content.remove(ligne)
    cyan("}}Permutation effectuee}}")
    
    
def remove(line,ligne,content,iterator):
    line_index = int(line[-1]) - 1
    content.remove(content[line_index])
    content.remove(ligne)
    iterator -= 2
    cyan("~~Suppression effectuee~~")

def blank(line,ligne,content):
    line_index = int(line[-1]) - 1
    content.insert(line_index,"")
    content.remove(ligne)
    cyan("~~Ligne vide insérée~~")

def inserti(line,ligne,content):
    line_index = int(line[-1]) - 1
    if line[-3] != "+i":
        insertion = line[-3].replace("_"," ")
    else:
        insertion = input(input_cyan("insert> "))
        
    content.insert(line_index,insertion)
    content.remove(ligne)
    cyan("~~Ligne inseree~~")

def move(line,ligne,content):
    first_index = int(line[0]) - 1
    last_index = int(line[4]) - 1
    print(line)
    if line[-1] != "-a":
        content.insert(last_index,content[first_index])
    else:
        content.insert(last_index+1,content[first_index])
    if first_index > last_index:
        first_index += 1
    del content[first_index]
    content.remove(ligne)
    cyan("++Deplacement effectue++")

def indent(line,ligne,content):
    global output
    line_index =  int(line[-1]) - 1
    temp = content[line_index].replace("\t","")
    temp = content[line_index].lstrip()
    if "_" in line[-3]:
        tab = line[-3].split("_")
        spacesnumber = int(tab[-1])
        result = " " * spacesnumber + temp
        content[line_index] = result
        output = ""
    elif line[-3] == "?":
        without_spaces = content[line_index].strip(" ")
        number_of_spaces = len(content[line_index]) - len(without_spaces)
        output = f"Line {line_index + 1} indented with {number_of_spaces} spaces"
    elif line[-3] == "?t":
        without_spaces = content[line_index].strip("\t")
        number_of_spaces = len(content[line_index]) - len(without_spaces)
        output = f"Line {line_index + 1} indented with {number_of_spaces} tabs"
    else:
        tabstime = int(line[-3])
        result = "\t" * tabstime + temp
        content[line_index] = result
        output = ""

    content.remove(ligne)
    cyan("==Tabulation effectue==")

def ponctuate(line,ligne,content):
    line_index = int(line[-1]) - 1
    if line[-3] == "-b":
        result = line[-5] + content[line_index]
    elif line[-3] == "-a":
        result = content[line_index] + line[-5]
    content[line_index] = result
    content.remove(ligne)
    cyan("Ponctuation effectuee")

def empty(content):
    content = []

def looper(line,ligne,content):
    bounds = line[2].split("-")
    start = int(bounds[0]) - 1
    end = int(bounds[1]) - 1
    if "-" in line[4]:
        command = line[4].split("-")
    else:
        command = line[4]
        
    if command == "replace":
        cyan("--Remplacement--")
        replacement = input(input_cyan(f"Replace {start+1} to {end+1}> "))
        for i in range(start,end+1):
            content[i] = replacement
        cyan("::Remplacement effectue::")
    elif command[1] == "copy":
        line_index = int(command[0]) - 1
        replacement = content[line_index]
        for i in range(start,end+1):
            content[i] = replacement
        cyan("::Copie effectue::")
    elif command[1] == "swap":
        line_index = int(command[0]) - 1
        temp = ""
        for i in range(end,start,-1):
            temp = content[line_index]
            content[line_index] = content[i]
            content[i]= temp
        cyan("::Permutation effectue::")
    elif command[0] == "insert":
        if command[-1] != "+r":
            if command[-1] != "+i":
                insertion = command[-1].replace("_"," ")
            else:
               cyan("~~Insertion~~")
               insertion = input(input_cyan("insert> "))
            for i in range(start,end+1):
                content.insert(i,insertion)
        else:
            startline = int(command[1]) -1
            for i in range(start,end+1):
                content.insert(startline,content[i])
                startline += 1
        cyan("::Insertion  effectue::")
    elif command == "rangeinsert":
        if end != -1:
            for i in range(start,end+1):
                option = input(input_cyan(f"Line {i+1}> "))
                content.insert(i,option)
        else:
            it = start
            while 1:
                option = input(input_cyan(f"Line {it+1}> "))
                if option != "stop":
                    content.insert(it,option)
                else:
                    break
                it += 1
    elif command == "remove":
        for i in range(end,start-1,-1):
            content.remove(content[i])
        cyan("::Suppression  effectue::")
    content.remove(ligne)

def regex_replace(line,ligne,content):
    reg =  line[-1]
    occurences = 0
    if line[2] == "a":
        replacement = input(input_cyan("new> "))
        content.remove(ligne)
        cyan("--Remplacement--")
        for i in range(len(content)):
            if re.search(reg,content[i]):
                content[i] = re.sub(reg,replacement,content[i])
    else:
        content.remove(ligne)
        cyan("--Remplacement--")
        for i in  range(len(content)):
            if re.search(reg,content[i]):
                occurences += 1
                replacement = input(input_cyan(f"OC {occurences} - line {i+1}> "))
                if re.match("_\d",replacement):
                    sp = replacement.split("_")
                    spacelength = int(sp[-1])
                    replacement = re.sub("_\d"," " * spacelength,replacement)
                content[i] = re.sub(reg,replacement,content[i])
    cyan("::Remplacement effectué::")
   
def draw_interface(nom,content):
    system("clear")
    cyan(f"Nom de fichier: {nom}")
    vert("=Debut=")
    for index,element in enumerate(content):
        print(f"\033[1;32m{index+1}\033[1;36m {element}")
    
def command_tools(nom,ligne,content,iterator):
    line = re.split("( |:>|->|}>|~>|<>|>>|@replace|@copy|@swap|@remove|@blank|@insert)",ligne)
    out = 1
    try:
        if ":>" in line or "@replace" in line:
            replace(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        elif "->" in line or "@copy" in line:
            copy(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        elif "}>" in line or "@swap" in line:
            swap(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        elif "<>" in line or "@blank" in line:
            blank(line,ligne,content)
            draw_interface(nom,content)
            out = 1
        elif ">>" in line or "@insert" in line:
            inserti(line,ligne,content)
            draw_interface(nom,content)
            out = 1
        elif "~>" in line or "@remove" in line:
            remove(line,ligne,content,iterator)
            draw_interface(nom,content)
            out = 3
        elif ":R" in line or "@Replace" in line:
            regex_replace(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        
        elif "()" in line or "@looper" in line:
            looper(line,ligne,content)
            draw_interface(nom,content)
            out = 4
        elif "\+" in line or "@to" in line:
            move(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        elif "\-" in line or "@indent" in line:
            indent(line,ligne,content)
            if output != "":
                input(input_cyan(output))
            draw_interface(nom,content)
            out = 2
        elif "\&" in line or "@ponctuate" in line:
            ponctuate(line,ligne,content)
            draw_interface(nom,content)
            out = 2
        elif "@empty" in line:
            empty(content)
            draw_interface(nom,content)
            out = 3
        else:
            out = 1

        if ligne == ":q":
            vert("=Fin=")
            content.pop()
            out = 0
        return out
    except IndexError:
        content.pop()
    #except:
    #    input("Erreur dans la commande precedente")
    #    content.pop()
