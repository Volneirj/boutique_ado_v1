print('custom_storages.py is being loaded')
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    print('loading static')
    location = 'static'

class MediaStorage(S3Boto3Storage):
    location = 'media'