# encoding: utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
from notifo import Notifo, send_message

class TestNotifyUser(unittest.TestCase):

    def setUp(self):
        self.provider = "test_provider"
        self.provider_banned = "test_provider_msg_banned"
        self.user = "test_user"
        self.sender = "test_user2"
        self.banned = "test_user_banned"
        self.banned_token = "x128302fd34a60bf7e5670d003d858e6fb06ce6bf"
        self.sender_token = "x633a05b18f7f65bf461ffb3900c6eb70eaafb0ed"
        self.provider_token = "74515bc044df6594fbdb761b12a42f8028e14588"
        self.provider_banned_token = "e34e447385fb4ff9084204cba19731d29c2afd78"
        self.user_token = "xbb8b3cba22a5f3d64fd404a07e84cdbb0c3566e5"

    def test_message(self):
        res = send_message(self.sender, self.sender_token,
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

    def test_message_with_object(self):
        res = Notifo(self.sender, self.sender_token).send_message(
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

    def test_message_banned(self):
        res = send_message(self.banned, self.banned_token,
                                to=self.user, msg="foo test")
        self.assertEqual(1102, res["response_code"])

    def test_message_provider(self):
        res = send_message(self.provider, self.provider_token,
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

    def test_message_provider_banned(self):
        res = send_message(self.provider_banned, self.provider_banned_token,
                                to=self.user, msg="foo test")
        self.assertEqual(1102, res["response_code"])

if __name__ == '__main__':
    unittest.main()
