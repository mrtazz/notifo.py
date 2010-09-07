# encoding: utf-8
import unittest
import os
import sys
sys.path.append(os.getcwd())
from notifo import Notifo, send_notification

class TestNotifyUser(unittest.TestCase):

    def setUp(self):
        self.provider = "test_provider"
        self.user = "test_user"
        self.provider_token = "74515bc044df6594fbdb761b12a42f8028e14588"
        self.user_token = "xbb8b3cba22a5f3d64fd404a07e84cdbb0c3566e5"

    def test_notify_self(self):
        res = send_notification(self.user, self.user_token,
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

    def test_notify_self_with_object(self):
        res = Notifo(self.user, self.user_token).send_notification(
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

    def test_message_with_label(self):
        res = send_notification(self.user, self.user_token,
                                to=self.user, msg="foo test", label="label")
        self.assertEqual(2201, res["response_code"])

    def test_message_with_plain_args(self):
        res = send_notification(self.user, self.user_token,
                                self.user, "foo test", "label")
        self.assertEqual(2201, res["response_code"])

    def test_message_with_title(self):
        res = send_notification(self.user, self.user_token,
                                to=self.user, msg="foo test", title="title")
        self.assertEqual(2201, res["response_code"])

    def test_message_with_callback(self):
        res = send_notification(self.user, self.user_token,
                                to=self.user, msg="foo test",
                                uri="http://example.org")
        self.assertEqual(2201, res["response_code"])

    def test_message_from_provider(self):
        res = send_notification(self.provider, self.provider_token,
                                to=self.user, msg="foo test")
        self.assertEqual(2201, res["response_code"])

if __name__ == '__main__':
    unittest.main()
