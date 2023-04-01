import os
import logging
from colorama import Fore, Style
from profile_parser import get_server_address_and_port_from_profile
from ip_checker import is_ip_accessible


def batch_verify_profiles(profiles_dir, username, password):
    results = []

    files = sorted(os.listdir(profiles_dir))
    for file in files:
        if file.endswith('.ovpn'):
            file_path = os.path.join(profiles_dir, file)
            logging.info(f"Processing {file} ...")
            server_address, server_port = get_server_address_and_port_from_profile(file_path)
            accessibility = is_ip_accessible(server_address, server_port, file_path, username, password)
            accessibility_str = "Yes" if accessibility else "No"
            color = Fore.GREEN if accessibility else Fore.RED
            logging.info(
                f"File: {file}, Server Address: {server_address}, Port: {server_port}, Accessible: {color}{Style.BRIGHT}{accessibility_str}{Style.RESET_ALL}")
            results.append((file, server_address, server_port, accessibility))

    return results
