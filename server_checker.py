import pexpect
import tempfile
import logging

from profile_parser import get_server_address_and_port_from_profile


def is_profile_usable(profile_file_path, username, password):
    server_address, server_port = get_server_address_and_port_from_profile(profile_file_path)

    logging.info(f"Checking accessibility for {profile_file_path}...")

    try:
        with tempfile.NamedTemporaryFile('w', suffix='.auth') as auth_file:
            auth_file.write(f"{username}\n{password}")
            auth_file.flush()

            logging.debug(f"-- Username: {username}")
            logging.debug(f"-- Password: {password}")

            cmd = ['openvpn', '--config', profile_file_path, '--auth-user-pass', auth_file.name, '--connect-timeout',
                   '5', '--connect-retry', '1', '--connect-retry-max', '1']

            logging.debug(f"-- command: {' '.join(cmd)}")

            child = pexpect.spawn(' '.join(cmd), timeout=30)
            output = child.read().decode('utf-8')
            child.expect(pexpect.EOF)

            logging.debug(f"-- output: {output}")

            if 'VERIFY OK' not in output:
                logging.warning(f"Not accessible: {server_address}:{server_port}")
                return False
            else:
                logging.info(f"Accessible: {server_address}:{server_port}")
                return True

    except Exception as e:
        logging.error(f"Exception encountered: {e}")
        return False
