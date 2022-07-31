from storages.backends.s3boto3 import S3Boto3Storage

"""
This will allow AWS to correctly connect with Django and function appropriately.
"""

class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "private"


class MediaStore(S3Boto3Storage):
    location = "media"
    file_overwrite = False
