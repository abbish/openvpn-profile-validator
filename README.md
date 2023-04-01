# openvpn-profile-validator
Check whether a given OpenVPN profile can be used in the your network in batches

usage: main.py [-h] (-d DIRECTORY | -f FILE) -u USERNAME -p PASSWORD

```shell
# validate profiles from directory
python3 main.py -d test_profiles -u OPENVPN_USERNAME -p OPENVPN_PASSWORD

```
