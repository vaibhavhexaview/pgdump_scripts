#!/usr/bin/python

import os
import boto3
from subprocess import PIPE,Popen

#schema = 'firm_1'
#table = 'investment_info'

def dump_table(host,database,user,password,schema,table):

    command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t {3}.{4} -Fp -f {3}_{4}.sql'.format(host,database,user,schema,table)
    p = Popen(command, shell=True, env={**os.environ, "PGPASSWORD": password})
    return p.communicate('{}\n'.format(password))

def upload(schema, table):

    session = boto3.Session(
       aws_access_key_id=os.getenv("AWS_AK"),
       aws_secret_access_key=os.getenv("AWS_SK"),
     )

    s3 = session.resource('s3')

    s3.meta.client.upload_file(Filename='{0}_{1}.sql'.format(schema, table), Bucket='cloudfrontpractic', Key='{0}_{1}.sql'.format(schema, table))

def main():
    dump_table('172.18.0.2','Portfolio','admin','admin','firm_1','investment_info')
    upload('firm_1', 'investment_info')

if __name__ == "__main__":
    main()

