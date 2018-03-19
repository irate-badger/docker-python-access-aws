import encode
import time

# This used the methods from Amazons REST API for S3
# https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html


def s3():
    return True


def create_url(path, expire, aws_access_key, aws_secret_key):
    print "\n\n\n***Generating the encoded url"
    try:
        bucket, file_path = _split_paths(path)
        print "Expiring after {expire}".format(expire=expire)
        expiration = _calculate_expiration(expire)
        return _calculate(bucket, file_path, expiration, aws_access_key, aws_secret_key)
    except AttributeError:
        return "The path is not long enough, did we miss the bucket?"


def _split_paths(path):
    paths = path.split("/")
    if len(paths) < 2:
        raise AttributeError

    bucket = paths[0]
    paths.remove(bucket)
    file_path = '/'.join(paths)

    return bucket, file_path


def _calculate(bucket, file_path, expiration, aws_access_key, aws_secret_key):
    url = "GET\n\n\n{expiration}\n/{bucket}/{file_path}".format(expiration=str(expiration),
                                                                bucket=bucket,
                                                                file_path=file_path)
    print "Generated {url} from {expiration} and {file_path}".format(url=url,
                                                                     expiration=expiration,
                                                                     file_path=file_path)
    print "Encoding url with {S3PROXY_AWS_SECRET_KEY}".format(S3PROXY_AWS_SECRET_KEY=aws_secret_key)
    signature = encode.sha1(url, aws_access_key)
    s3_url = "https://{bucket}.s3.amazonaws.com/{file_path}?AWSAccessKeyId={S3PROXY_AWS_ACCESS_KEY}" \
             "&Expires={expiration}&Signature={signature}"
    return s3_url.format(bucket=bucket, file_path=file_path, S3PROXY_AWS_ACCESS_KEY=aws_access_key,
                         expiration=expiration, signature=signature)


def _calculate_expiration(expire, current_time=-1):
    if current_time == -1:
        current_time = int(time.time())
    expiration = current_time + expire
    print "Expiring after {expiration}, calculated from {current_time} and {expire}"\
        .format(expiration=expiration, current_time=current_time, expire=expire)
    return expiration
