import os
import json
from utility import jsonReader,existanceCheck
from fileclone import FileClone

class DirClone:
    def __init__(self, template_folder):
        self.TEMPLATE_FOLDER = template_folder

    def createDir(self, templatedir, *args):
        replacement_params = {}
        #---------> >  >
        # Read the config.json
        #---------> >  >
        templatedir = templatedir + ".template"
        path = os.path.join(self.TEMPLATE_FOLDER , templatedir)
        
        existanceCheck(path, 2)
        replacement_params_file_path = os.path.join(path, "replace.json")
        if os.path.exists(replacement_params_file_path):
            f = open(replacement_params_file_path)
            replacement_params = json.load(f)
            for k in replacement_params.keys():
                replacement_params[k] = input(f"{k[2:-2]} : ")
        
        config_file_path = os.path.join(path, "config.json")
        existanceCheck(config_file_path, 3)

        config = jsonReader(config_file_path, replacement_params)
        #---------> >  >
        # Create Directories & Files
        #---------> >  >
        for d in config['dir']:
            os.mkdir(d)

        fileGen = FileClone(path)
        for f in config['files']:
            fileGen.createFile(f['template'], f['location'])
        
        return 


    def addDirTemplate(self, dirloc: str, template_name: str):
        # Reverse of CreateDir
        # Open the directory, explor all subdirectories and files
        # listout all the directies
        # Create template from all the files
        # Create config.json
        # Create replace.json

        existanceCheck(dirloc, 3)
        if os.path.exists(os.path.join(self.TEMPLATE_FOLDER, template_name + ".template")):
            print("Template already exists")
            exit(1)
        
        config = {
            "dir" : [dirloc],
            "files" : []
        }
        path = os.path.join(self.TEMPLATE_FOLDER, template_name + ".template")
        os.mkdir(path)
        
        fileGen = FileClone(path)
        
        for root, dirs, files in os.walk(dirloc):
            for d in dirs:
                config["dir"].append(os.path.join(root, d))
            for f in files:
                fileGen.addTemplate(f.split('.')[0], os.path.join(root, f))
                config["files"].append({
                    "template" : f.split('.')[0],
                    "location" : os.path.join(root, f)
                })
        
        # saving config.json
        config_file_path = os.path.join(path, "config.json")
        with open(config_file_path, "w") as f:
            json.dump(config, f, indent=4)
        return
            
                
