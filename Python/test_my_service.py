import unittest

from my_service import *

class MyServiceTest(unittest.TestCase):
    name = 'Earl'
    token = 'e4r1_t0k3n'
    def test_invalidSSOTokenIsRejected(self):
        SingleSignOnRegistry
        service = MyService(SingleSignOnRegistry())
        response = service.handle_request(Request(self.name, self.token))
        self.assertEqual(None, response)
        
        
if __name__ == "__main__":
    unittest.main()