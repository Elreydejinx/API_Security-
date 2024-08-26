import unittest
from utils.util import encode_token, decode_token

class TestTokenFunctions(unittest.TestCase):
    def test_encode_token(self):
        token = encode_token(1)
        self.assertInstance(token, str)

    
    def test_decode_token(self):
        token = encode_token(1)
        payload = decode_token(token)
        self.assertEqual(payload['user_id'], 1)

if __name__== '__main__':
    unittest.main()

    
