# create shell header
#!/bin/bash
source ./venv/bin/activate
pip install -r requirements.txt
python3 ./main.py -d ./test_profiles -u testusername -p testpassword -r -t 100