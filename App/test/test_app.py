from nose.tools import *
import unittest
import os

# Setting environment variables before App.app attempts to access them. We should probably just set app in a before
os.environ['S3PROXY_AWS_ACCESS_KEY'] = 'ACCESSKEY112233445566'
os.environ['S3PROXY_AWS_SECRET_KEY'] = 'SECRETKEY1122334455667788990011223344556'

# Fails PEP-8, but we need to initialise the app after the env has been set
import App.app as app


class TestApp(unittest.TestCase):

    def test_always_true(self):
        self.assertTrue(True)
