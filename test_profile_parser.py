import unittest
from profile_parser import get_server_address_and_port_from_profile


class TestProfileParser(unittest.TestCase):

    def test_get_server_address_and_port_from_profile(self):
        server_address, server_port = get_server_address_and_port_from_profile(
            'test_profiles/za-jnb.prod.surfshark.com_udp.ovpn')
        self.assertEqual(server_address, 'za-jnb.prod.surfshark.com')
        self.assertEqual(server_port, 1194)


if __name__ == '__main__':
    unittest.main()
