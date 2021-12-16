#!/usr/bin/python

import os
from subprocess import PIPE,Popen

def dump_table(host,database,user,password,schema,table):

    command = 'pg_dump -h {0} -d {1} -U {2} -p 5432 -t {3}.{4} -Fc -f {3}.dump'.format(host,database,user,schema,table)

   # p = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    p = Popen(command, shell=True, env={**os.environ, "PGPASSWORD": password})
    return p.communicate('{}\n'.format(password))

def main():
    dump_table('172.22.0.3','Portfolio','admin','admin','Firms','Firms_Info')

if __name__ == "__main__":
    main()
