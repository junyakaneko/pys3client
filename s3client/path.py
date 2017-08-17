import os
import botocore
import s3client


__author__ = 'Junya Kaneko <jyuneko@hotmail.com>'


def abspath(path):
    return os.path.normpath(os.path.join(s3client.getcwd(), path))


def exists(path):
    path = abspath(path)[1:]
    try:
        s3client._s3client.Object(s3client.s3conf['bucket'], path).load()
    except botocore.exceptions.ClientError as e:    
        bucket = s3client._s3client.Bucket(s3client.s3conf['bucket'])
        keys = bucket.objects.filter(Delimiter='/', MaxKeys=1, Prefix=path + '/')
        if sum(1 for _ in keys):
            return True
        else:
            return False
    return True
