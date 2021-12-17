import os
import boto3


#session = boto3.Session(
#    aws_access_key_id=os.environ['%env.AWS_AK%'],
#    aws_secret_access_key=os.environ['%env.AWS_SK%'],
#)

session = boto3.session.Session(profile_name='ankit9')
s3 = session.resource('s3')

s3.meta.client.upload_file(Filename='pg_backup.sql', Bucket='cloudfrontpractic', Key='pg_backup.sql')
