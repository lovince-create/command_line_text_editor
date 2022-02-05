import re
from couleur import *
def replace(line,ligne,content):
    line_index = int(line[-1]) - 1
    cyan("--Remplacement--")
    cyan(f"old> {content[line_index]}")
    content[line_index] = input(input_cyan("new> "))
    cyan("::Remplacement effectué::")
    content.remove(ligne)
        
def copy(line,ligne,content):
    first_index = int(line[0]) - 1
    last_index = int(line[-1]) - 1
    content[last_index]  = content[first_index]
    content.remove(ligne)
    cyan("--Copie effectuée--")
        
def swap(line,ligne,content):
    first_index = int(line[0]) - 1
    last_index = int(line[-1]) - 1
    content[first_index], content[last_index] = content[last_index],content[first_index]
    content.remove(ligne)
    cyan("}}Permutation effectuée}}")
    
    
def remove(line,ligne,content,iterator):
    line_index = int(line[-1]) - 1
    content.remove(content[line_index])
    content.remove(ligne)
    iterator -= 2
    cyan("~~Suppression effectuée~~")
                
def command_tools(ligne,content,iterator):
    line = re.split("( |:>|->|}>|~>|@replace|@copy|@swap|@remove)",ligne)
    try:
        if ":>" in line or "@replace" in line:
            replace(line,ligne,content)
        elif "->" in line or "@copy" in line:
            copy(line,ligne,content)
        elif "}>" in line or "@swap" in line:
            swap(line,ligne,content)
        elif "~>" in line or "@remove" in line:
            remove(line,ligne,content,iterator)
            
        if ligne == ":q":
            vert("=Fin=")
            content.pop()
            return 0
        else:
            return 10
    except IndexError:
        content.remove(ligne)
        i -= 1
