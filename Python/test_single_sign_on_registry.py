import unittest
from mock import MagicMock
import single_sign_on
from single_sign_on import SingleSignOnRegistry, SSOToken

class SsoTest(unittest.TestCase):
	name = 'Earl'
	token = SSOToken('e4r1_t0k3n')
	credentials = 'Earl#passwd'

	def test_register_new_session_for_valid_credentials(self):
		single_sign_on.credentials_are_valid = MagicMock(return_value=True)
		single_sign_on.generate_token = MagicMock(return_value=self.token)
		sso_registry = SingleSignOnRegistry()
		response_token = sso_registry.register_new_session(self.credentials)

		single_sign_on.credentials_are_valid.assert_called_once_with(self.credentials)
		single_sign_on.generate_token.assert_called_once_with()

		self.assertEquals(self.token, response_token)



if __name__ == "__main__":
	unittest.main()