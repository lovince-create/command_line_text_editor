from os import system
import re
def run_by_extension(source_file,ext):
    namelist = re.split("[/.]",source_file)
    namelist_with_path = source_file.split(".")
    beforedot = namelist[0]
    if ext == "py":
        system(f"python3 {source_file} > output.txt")
    elif ext == "rb":
        system(f"ruby {source_file} > output.txt")
    elif ext == "js":
        system(f"js {source_file} > output.txt")
    elif ext == "sh":
        system(f"bash {source_file} > output.txt")
    elif ext == "php":
        system(f"php {source_file} > output.txt")
    elif ext == "txt":
        print("File texte")
    #Compiled languages

    """elif ext == "c":
        system(f"gcc {source_file} -o {beforedot} && ./{beforedot} > output.txt")"""
    file = open("output.txt","r").read()
    return file
