#!/usr/bin/env python3
import argparse
from config import TEMPLATE_FOLDER
from dirclone import DirClone
from fileclone import FileClone

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Template generator V1.0',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
    )

    parser.add_argument('-f','--filename', required = False)       # positional argument
    parser.add_argument('-t', '--template', required = False)      # option that takes a value
    parser.add_argument('-a', '--add', required = False)
    parser.add_argument('-l', '--list',
                        action='store_true', required = False)
    parser.add_argument('-d', '--dtemplate', required= False)

    args = parser.parse_args()
    # print(args.filename, args.template, args.add, args.list)
    if args.list:
        templates = FileClone(TEMPLATE_FOLDER).all_templates()
        for template in templates:
            print(template)
        exit(1)
    if (args.add != None) and (args.filename != None):
        template = FileClone(TEMPLATE_FOLDER)
        template.addTemplate(args.add, args.filename)
        exit(1)
    if args.template :
        template = FileClone(TEMPLATE_FOLDER)
        template.createFile( args.template , args.filename )
        exit(1)
    if args.dtemplate :
        template = DirClone(TEMPLATE_FOLDER)
        template.createDir(args.dtemplate)
        exit(1)
    print("Uses `--help` for more information")
    