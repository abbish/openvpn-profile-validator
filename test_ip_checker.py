import unittest
from ip_checker import is_ip_accessible


class TestIPChecker(unittest.TestCase):

    def test_is_ip_accessible_with_ip(self):
        self.assertTrue(is_ip_accessible("8.8.8.8", 53, None, None, None))

    def test_is_ip_accessible_with_domain(self):
        self.assertTrue(is_ip_accessible("example.com", 80, None, None, None))

    def test_is_ip_accessible_with_openvpn(self):
        # Replace these values with your own valid settings.
        valid_openvpn_profile = "path/to/your/valid.ovpn"
        valid_username = "your_username"
        valid_password = "your_password"

        # Replace these values with an unreachable OpenVPN server.
        invalid_openvpn_profile = "path/to/your/invalid.ovpn"

        self.assertTrue(is_ip_accessible(None, None, valid_openvpn_profile, valid_username, valid_password))
        self.assertFalse(is_ip_accessible(None, None, invalid_openvpn_profile, valid_username, valid_password))


if __name__ == '__main__':
    unittest.main()
