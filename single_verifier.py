import logging
from colorama import init, Fore, Back, Style
from profile_parser import get_server_address_and_port_from_profile
from ip_checker import is_ip_accessible

init()


def single_verify_profile(file_path):
    logging.info(f"Processing {file_path} ...")
    server_address, server_port = get_server_address_and_port_from_profile(file_path)
    accessibility = is_ip_accessible(server_address, server_port)
    accessibility_str = "Yes" if accessibility else "No"
    color = Fore.GREEN if accessibility else Fore.RED
    logging.info(
        f"File: {file_path}, Server Address: {server_address}, Port: {server_port}, Accessible: {color}{Style.BRIGHT}{accessibility_str}{Style.RESET_ALL}")
    return file_path, server_address, server_port, accessibility
