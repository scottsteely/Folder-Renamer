import os
import shutil
from pathlib import Path

for root, dirs, files in os.walk("C:\\projects\\Folder renamer\\data", topdown=False):
   for name in files:
    #seperates artist from song with -
    result = [x.strip() for x in name.split('-')]
    result[1] = result[1].replace(' [Z Karaoke]', '')
    
    #clean up song with no artist
    if (result[0].find('.') != -1):
        result.append(result[0])
        result[0] = 'Unknown'
    
    parent_path = (f'{Path(root).parent}\{result[0]}')

    if not os.path.exists(parent_path):
        os.makedirs(parent_path)

    if os.path.exists(parent_path):
        # move files into created directory    
        old = (os.path.join(root, name))
        new = (os.path.join(parent_path, result[1]))
        shutil.move(old, new)
