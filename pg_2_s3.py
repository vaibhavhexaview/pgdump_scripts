import boto3

session = boto3.Session(
    aws_access_key_id=%env.AWS_AK%,
    aws_secret_access_key=%env.AWS_SK%,
)
s3 = session.resource('s3')

s3.meta.client.upload_file(Filename='pg_dumps', Bucket='cloudfrontpractic', Key='pg_dumps.sql')
