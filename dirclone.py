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


    def addDirTemplate(self):
        
        pass
