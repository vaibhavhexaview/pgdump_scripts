#!/usr/bin/python

import os
from subprocess import PIPE,Popen

def dump_table(host,database,user,password,schema,table):

    command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t {3}.{4} -Fp -f {3}.sql'.format(host,database,user,schema,table)

   # p = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    p = Popen(command, shell=True, env={**os.environ, "PGPASSWORD": password})
    return p.communicate('{}\n'.format(password))

def main():
    dump_table('172.18.0.2','Portfolio','admin','admin','firms','*')

if __name__ == "__main__":
    main()
