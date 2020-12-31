import os
from pathlib import Path
import shutil

from extensions import Extensions


def organize_files(folders):

    userHomeDir = str(Path.home())

    for folder in folders:

        targetDir = os.path.join(userHomeDir, folder)

        for key, data in Extensions.items():

            for file in os.listdir(targetDir):
                file_extension = os.path.splitext(file)[1]
                file_extension = file_extension[1:].lower()

                path_to_file = os.path.join(targetDir, file)
                destination_dir = os.path.join(targetDir, key)
                destination_path = os.path.join(destination_dir, file)

                if file_extension in data:

                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                
                    shutil.move(path_to_file, destination_path)

        print(f'Files organized succesfully in: {folder}')    


            

        

        


