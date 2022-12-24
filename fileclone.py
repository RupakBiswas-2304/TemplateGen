import os
from utility import existanceCheck

class FileClone:
    def __init__(self, template_folder):
        self.TEMPLATE_FOLDER = template_folder

    def createFile(self, template, filename):
        template = template + ".template"
        path = os.path.join( self.TEMPLATE_FOLDER, template)

        existanceCheck(path, 1)

        with open(path, "r") as f:
            content = f.read()
        with open(filename, "w") as f:
            f.write(content)
        return

    def all_templates(self):
        templates = os.listdir(self.TEMPLATE_FOLDER)
        templates = [x[:-9] for x in templates]
        return templates

    def addTemplate(self, template, filename):
        print("flag")
        template = template + ".template"
        path = os.path.join( self.TEMPLATE_FOLDER, template)
        if os.path.exists(path):
            print("Template already exists")
            exit(1)
        with open(filename, "r") as f:
            content = f.read()
        with open(path, "w") as f:
            f.write(content)