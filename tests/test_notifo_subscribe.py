# encoding: utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
from notifo import Notifo, subscribe_user

class TestSubscribeUser(unittest.TestCase):

    def setUp(self):
        self.provider = "test_provider"
        self.token = "74515bc044df6594fbdb761b12a42f8028e14588"

    def test_subscribe(self):
        res = subscribe_user(self.provider, self.token, "test_user")
        self.assertEqual(res["response_code"], 2202)

    def test_subscribe_with_object(self):
        res = Notifo(self.provider, self.token).subscribe_user("test_user")
        self.assertEqual(res["response_code"], 2202)

    def test_subscribe_failed(self):
        res = subscribe_user(self.provider, "token", "test_user")
        self.assertEqual(res["response_code"], 401)

if __name__ == '__main__':
    unittest.main()
