import hmac
import hashlib
import urllib
import base64


def sha1(url, aws_secret_key):
    h = hmac.new(aws_secret_key, url, hashlib.sha1)
    signature = urllib.quote_plus(base64.encodestring(h.digest()).strip())
    return signature


# Will need to implement: https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html
def sig_v4():
    return False
