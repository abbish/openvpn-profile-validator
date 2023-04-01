import argparse
from batch_verifier import batch_verify_profiles
from single_verifier import single_verify_profile

import colorama

import logging
import sys

from summery_table import print_summary_table

colorama.init(autoreset=True)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

loggerHandler = logging.StreamHandler(sys.stdout)
loggerHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loggerHandler.setFormatter(formatter)
logger.addHandler(loggerHandler)

parser = argparse.ArgumentParser(description='OpenVPN Profile Validator')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', help='Directory containing OpenVPN profile files')
group.add_argument('-f', '--file', help='Single OpenVPN profile file')
parser.add_argument('-u', '--username', help='OpenVPN username', required=True)
parser.add_argument('-p', '--password', help='OpenVPN password', required=True)
parser.add_argument('-t', '--num_threads', help='Number of threads to use for parallel processing', type=int, default=5)

args = parser.parse_args()

if args.directory:
    results = batch_verify_profiles(args.directory, args.username, args.password, args.num_threads)
else:
    results = single_verify_profile(args.file, args.username, args.password)

print_summary_table(results)
