# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:58:00 2021

@author: Nisrine
"""
import redis 
import string
import random
import sha3
import time
import aes256
import bcryct2

rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)
rsalt_global = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)

rsalt_global.flushdb()

f = open("10.txt", "a")

lists=[]

#listss=[]
#i=0
#for i in range(10000):  
    #listss=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    #lists.append(listss)
#stockage en plain
lists= random.choices(string.ascii_uppercase, k=10000)
fun_type= 'plain'
t0= time.perf_counter()
for i in range(len(lists)): 
        rserver.set(i, lists[i])
t_ = time.perf_counter()

temps= t_-t0
f.write("%s %s\n" % (str(fun_type) , str(temps) ))

def fun_hashage(xfun_hashage, fun_type): 
      
    t1 = time.perf_counter()
    for i in range(len(rserver.keys())): 
        mdp_hash= xfun_hashage(rserver.get(rserver.keys()[i]))
    t2=  time.perf_counter()
    
    temps= t2-t1
    f.write("%s %s\n" % (str(fun_type) , str(temps) ))
    return temps, mdp_hash

#plain= fun_hashage(rserver.set, 'plain')

sha= fun_hashage(sha3.fun_sha256, 'sha256')

sha_sel= fun_hashage( sha3.fun_sha256_selglobal, 'sha256+sel')

sha_sel_user= fun_hashage(sha3.fun_sha265_sels, 'sha256+sel+user')

bcrypt= fun_hashage(bcryct2.fun_bcrypt, 'bcrypt')

aes= fun_hashage( aes256.fun_aes, 'aes')

f.close()

