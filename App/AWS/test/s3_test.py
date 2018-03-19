from nose.tools import *
import unittest

# Fails PEP-8, but we need to initialise the app after the env has been set
import App.AWS.s3 as app


# Setting environment variables before App.app attempts to access them. We should probably just set app in a before
AWS_ACCESS_KEY = 'ACCESSKEY112233445566'
AWS_SECRET_KEY = 'SECRETKEY1122334455667788990011223344556'


class TestApp(unittest.TestCase):

    def test_always_true(self):
        self.assertTrue(True)

    def test_calculate(self):
        example_url = "https://mybucket.s3.amazonaws.com/myfolder/myfile?" \
                      "AWSAccessKeyId=ACCESSKEY112233445566&Expires=1480551000&Signature=XUrpMMzlztHt0WZLTDmLR5Erdds%3D"
        bucket = "mybucket"
        file_path = "myfolder/myfile"
        expiry = app._calculate_expiration(600, 1480550400)
        response = app._calculate(bucket, file_path, expiry, AWS_ACCESS_KEY, AWS_SECRET_KEY)
        self.assertEqual(example_url, response,
                         "The response wasn't expected. Recieved {response} expected {example_url}"
                         .format(response=response, example_url=example_url))

    def test_calculate_expiration(self):
        expiry = app._calculate_expiration(600, 1480550400)
        self.assertEqual(expiry, 1480551000, "Times were not added correctly")

    def test_split_paths_in_folder(self):
        path = "mybucket/myfolder/myfile"
        bucket, file_path = app._split_paths(path)
        self.assertEqual(bucket, "mybucket", "Bucket is not expected")
        self.assertEqual(file_path, "myfolder/myfile", "Filename and path is not expected")

    def test_split_paths(self):
        path = "mybucket/myfile"
        bucket, file_path = app._split_paths(path)
        self.assertEqual(bucket, "mybucket", "Bucket is not expected")
        self.assertEqual(file_path, "myfile", "Filename and path is not expected")

    @raises(AttributeError)
    def test_split_paths_missing_bucket(self):
        path = "myfile"
        bucket, file = app._split_paths(path)