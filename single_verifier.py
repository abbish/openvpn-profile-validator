import logging
from colorama import init, Fore, Style
from server_checker import is_profile_usable

init()


def single_verify_profile(file_path, username, password):
    logging.info(f"Processing {file_path} ...")
    accessibility = is_profile_usable(file_path, username, password)
    color = Fore.GREEN if accessibility else Fore.RED
    accessibility_str = "Yes" if accessibility else "No"
    accessibility_output_str = f"{color}{Style.BRIGHT}{accessibility_str}{Style.RESET_ALL}"

    logging.info(
        f"File: {file_path}, Accessible: {accessibility_output_str}")
    return file_path, accessibility_output_str
