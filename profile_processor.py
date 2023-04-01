import logging

import os
import shutil


def remove_inaccessible_profiles(results, trash_folder):
    os.makedirs(trash_folder, exist_ok=True)
    for item in results:
        if not item['accessibility']:
            file_path = item['file_name']
            logging.info(f"Moving {file_path} to trash folder...")

            if os.path.exists(file_path):
                shutil.move(file_path, os.path.join(trash_folder, os.path.basename(file_path)))
                logging.info(f"Moved {file_path} to {trash_folder}")
            else:
                logging.error(f"{file_path} does not exist")
