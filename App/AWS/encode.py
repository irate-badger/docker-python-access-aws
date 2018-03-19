import hmac
import hashlib
import urllib
import base64


def sha1(url, aws_secret_key):
    h = hmac.new(aws_secret_key, url, hashlib.sha1)
    signature = urllib.quote_plus(base64.encodestring(h.digest()).strip())
    return signature

