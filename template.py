import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

list_of_file = [
    "src/__init__.py",
    "src/hello.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for file in list_of_file:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the filename {filename}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
            logging.info(f"Creating empty file {file}")

    else:
        logging.info(f"File {file} already exists")