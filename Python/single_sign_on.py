class SingleSignOnRegistry:

	def register_new_session(self, credentials):
		token = None
		if credentials_are_valid(credentials):
			token = generate_token()

		return token

	def is_valid(self, token):
		"""Returns True if the token refers to a current session"""
		pass

	def unregister(self, token):
		"""Remove the given token from current sessions"""
		pass

class SSOToken:
	token = None
	def __init__(self, token):
		self.token = token

def credentials_are_valid(credentials):
	return True

def generate_token():
	pass

