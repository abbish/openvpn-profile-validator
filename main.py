import argparse
from batch_verifier import batch_verify_profiles
from single_verifier import single_verify_profile

parser = argparse.ArgumentParser(description='OpenVPN Profile Validator')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-d', '--directory', help='Directory containing OpenVPN profile files')
group.add_argument('-f', '--file', help='Single OpenVPN profile file')
parser.add_argument('-u', '--username', help='OpenVPN username', required=True)
parser.add_argument('-p', '--password', help='OpenVPN password', required=True)

args = parser.parse_args()

if args.directory:
    results = batch_verify_profiles(args.directory, args.username, args.password)
else:
    result = single_verify_profile(args.file, args.username, args.password)
    print(result)
