import socket
import subprocess
import tempfile
import time
import logging


def is_ip_accessible(server_address, server_port, profile_file_path, username, password):
    logging.info(f"Checking accessibility for {server_address}:{server_port}...")

    try:
        with tempfile.NamedTemporaryFile('w', suffix='.auth') as auth_file:
            auth_file.write(f"{username}\n{password}")
            auth_file.flush()

            cmd = ['openvpn', '--config', profile_file_path, '--auth-user-pass', auth_file.name, '--connect-timeout',
                   '5', '--connect-retry', '1', '--connect-retry-max', '1']
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(5)

            if proc.poll() is None:
                proc.terminate()
                proc.wait()
                logging.info(f"Accessible: {server_address}:{server_port}")
                return True
            else:
                logging.warning(f"Not accessible: {server_address}:{server_port}")
                return False
    except Exception as e:
        logging.warning(f"Exception encountered: {e}")
        return False
