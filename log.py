from datetime import datetime
import os

directory = os.getcwd()
timestamp = datetime.now().strftime("(%d/%m/%Y %H:%M:%S)")

print(directory)

def add_to_log():
    
    with open(f'{directory}/file.log', 'a') as log:
        print(timestamp, 
            'success',
            file=log,
            end='\n')
            

