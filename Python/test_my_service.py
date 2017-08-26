import unittest
from mock import MagicMock
from my_service import *

class MyServiceTest(unittest.TestCase):
    name = 'Earl'
    token = 'e4r1_t0k3n'

    def test_invalidSSOTokenIsRejected(self):
        SingleSignOnRegistry.is_valid = MagicMock(return_value = False)
        service = MyService(SingleSignOnRegistry())
        response = service.handle_request(Request(self.name, self.token))
        self.assertEqual(None, response)
        SingleSignOnRegistry.is_valid.assert_called_once_with(self.token)

    def test_validSSOTokenIsAccepted(self):
        SingleSignOnRegistry.is_valid = MagicMock(return_value=True)
        service = MyService(SingleSignOnRegistry())
        response = service.handle_request(Request(self.name, self.token))
        self.assertEqual('Hello ' + self.name + '!', response.text)
        SingleSignOnRegistry.is_valid.assert_called_once_with(self.token)

if __name__ == "__main__":
    unittest.main()