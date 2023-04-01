import argparse
import os

from batch_verifier import batch_verify_profiles
from profile_processor import remove_inaccessible_profiles
from single_verifier import single_verify_profile

import colorama

import logging
import sys

from summery_table import print_summary_table

parser = argparse.ArgumentParser(description='OpenVPN Profile Validator')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', help='Directory containing OpenVPN profile files')
group.add_argument('-f', '--file', help='Single OpenVPN profile file')
parser.add_argument('-u', '--username', help='OpenVPN username', required=True)
parser.add_argument('-p', '--password', help='OpenVPN password', required=True)
parser.add_argument('-t', '--num_threads', help='Number of threads to use for parallel processing', type=int, default=5)
parser.add_argument('--debug', help='Show debug message', action='store_true')
parser.add_argument('-r', '--remove', help='Automatically move invalid OpenVPN profile files to trash folder',
                    action='store_true')

args = parser.parse_args()

colorama.init(autoreset=True)

logLevel = logging.DEBUG if args.debug else logging.INFO
logger = logging.getLogger()
logger.setLevel(logLevel)

loggerHandler = logging.StreamHandler(sys.stdout)
loggerHandler.setLevel(logLevel)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loggerHandler.setFormatter(formatter)
logger.addHandler(loggerHandler)

trash_folder = 'trash'

if args.directory:
    trash_folder = os.path.join(args.directory, trash_folder)
    results = batch_verify_profiles(args.directory, args.username, args.password, args.num_threads)
else:
    trash_folder = os.path.join(os.path.dirname(args.file), trash_folder)
    results = single_verify_profile(args.file, args.username, args.password)

if args.remove:
    remove_inaccessible_profiles(results, trash_folder)

print_summary_table(results)
