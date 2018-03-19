import flask
import os
import argparse
import AWS.sns as sns
import AWS.s3 as s3

from flask import request
app = flask.Flask(__name__)

AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""

if os.environ.get('S3PROXY_AWS_ACCESS_KEY') is not None:
    AWS_ACCESS_KEY = os.environ['S3PROXY_AWS_ACCESS_KEY']

if os.environ.get('S3PROXY_AWS_SECRET_KEY') is not None:
    AWS_SECRET_KEY = os.environ['S3PROXY_AWS_SECRET_KEY']


@app.route('/')
def welcome_():
    return 'Try to provide a file that you would like encoding such as /mybucket/myfile to /s3/'


# You can distinguish in the code the different endpoints via request.method, which provides String values GET or POST
@app.route('/sns/<path:path>', methods=['GET', 'POST'])
def sns_(path):
    print(path)
    sns.sns()
    message = 'Calling SNS method: ' + request.method
    return message


@app.route('/s3/<path:path>', methods=['GET', 'POST'])
def s3_(path):
    return s3.create_url(path, request.args.get('expire', '60'), AWS_ACCESS_KEY, AWS_SECRET_KEY)


def _arg_parse():
    parser = argparse.ArgumentParser(description='Generate your own public, time limited S3 urls.')
    parser.add_argument('-a', '--ACCESS_KEY', type=str, help='Your AWS access key',
                        dest='AWS_ACCESS_KEY', required='True')
    parser.add_argument('-s', '--SECRET_KEY', type=str, help='Your AWS secret key',
                        dest='AWS_SECRET_KEY', required='True')

    _parsed_args = parser.parse_args()
    global AWS_ACCESS_KEY, AWS_SECRET_KEY
    AWS_ACCESS_KEY = _parsed_args.AWS_ACCESS_KEY
    AWS_SECRET_KEY = _parsed_args.AWS_SECRET_KEY


if __name__ == '__main__':
    _arg_parse()
    app.run()
