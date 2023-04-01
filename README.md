# openvpn-profile-validator
Check whether a given OpenVPN profile can be used in the your network in batches

```shell
usage: main.py [-h] (-d DIRECTORY | -f FILE) -u USERNAME -p PASSWORD

OpenVPN Profile Validator

optional arguments:
  -h, --help                            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY   Directory containing OpenVPN profile files
  -f FILE, --file FILE                  Single OpenVPN profile file
  -u USERNAME, --username USERNAME      OpenVPN username
  -p PASSWORD, --password PASSWORD      OpenVPN password

```

```shell
# validate profiles from directory
python3 main.py -d test_profiles -u OPENVPN_USERNAME -p OPENVPN_PASSWORD

```
