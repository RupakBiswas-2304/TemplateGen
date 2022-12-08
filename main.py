#!/usr/bin/env python3

import os
import sys
from config import TEMPLATE_FOLDER

def createFile(template, filename):
    template = template + ".template"
    path = os.path.join( TEMPLATE_FOLDER, template)
    if not os.path.exists(path):
        print("Template not found")
        exit(1)
    with open(path, "r") as f:
        content = f.read()
    with open(filename, "w") as f:
        f.write(content)
    print("Done")
    return

def all_templates():
    templates = os.listdir(TEMPLATE_FOLDER)
    templates = [x[:-4] for x in templates]
    return templates

def addTemplate(template, filename):
    template = template + ".template"
    path = os.path.join( TEMPLATE_FOLDER, template)
    if os.path.exists(path):
        print("Template already exists")
        exit(1)
    with open(filename, "r") as f:
        content = f.read()
    with open(path, "w") as f:
        f.write(content)

def help():
    print("Usage: main.py [filename] [-t template] [-a template] [-l]")
    print("Options:")
    print("\t-t template\tUse template")
    print("\t-a template\tAdd template")
    print("\t-l\t\tList all templates")
    print("If no options are given, the default template is used")
    return
    

if __name__ == "__main__":
    n = len(sys.argv)
    template = "basic"
    filename = "main.cpp"

    if n == 4:
        if sys.argv[1] == "-t":
            template = sys.argv[2]
            filename = sys.argv[3]
            createFile(template, filename)
        elif sys.argv[2] == "-t":
            filename = sys.argv[1]
            template = sys.argv[3]
            createFile(template, filename)
        elif sys.argv[1] == "-a":
            template = sys.argv[2]
            filename = sys.argv[3]
            addTemplate(template, filename)
        elif sys.argv[2] == "-a":
            filename = sys.argv[1]
            template = sys.argv[3]
            addTemplate(template, filename)
        else:
            filename = sys.argv[1]
    elif n > 4:
        print("Too many arguments")
        exit(1)
    elif n == 2 and sys.argv[1] == "-l":
        templates = all_templates()
        print("All templates:")
        for template in templates:
            print(template)
    elif n == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        help()
    exit(0)