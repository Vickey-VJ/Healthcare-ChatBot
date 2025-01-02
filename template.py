import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'app.py',
    'README.md',
    'research/trials.ipynb'
]

def create_files(list_of_files: list):
    for filepaths in list_of_files:
        filepath = Path(filepaths)
        filedir, filename = os.path.split(filepath)

        if filedir != '':
            os.makedirs(filedir, exist_ok=True)
            logging.info(f'Created directory: {filedir} for the file: {filename}')
    
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) and input(f'{filepath} already exists. Do you want to overwrite it? (y/n): ').lower() == 'y'):
            with open(filepath, 'w') as file:
                pass
                logging.info(f'Created empty file: {filepath}')

        else: logging.info(f'File: {filename} already exists. Skipped.')

create_files(list_of_files)