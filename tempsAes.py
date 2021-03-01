# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:29:41 2021

@author: Nisrine
"""

import redis 
import string
import random
import aes256
import time
import sys 
#Verification 10000 pour sha


rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rhashage= redis.StrictRedis(host="localhost", port=6379, db=4, decode_responses=True)
rnonce = redis.StrictRedis(host="localhost", port=6379, db=3, decode_responses=True)
rserver.flushdb()
rhashage.flushdb()
rnonce.flushdb()
#remplir une base en plain
f = open("10000_8.txt", "a")
#1 cara
#rnd_lists= random.choices(string.ascii_lowercase, k = 1000)
#8 cara
rnd_lists=[]
for i in range(10):  
    listss=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    rnd_lists.append(listss)
    
    
for i in range(len(rnd_lists)): 
    rserver.set(i, rnd_lists[i])

#hashage
for user in rserver.keys():
    
    mdp= rserver.get(user)
    mdp_hash, nonce= aes256.fun_aes(mdp)
    rhashage.set(user,mdp_hash)
    rnonce.set(user, nonce)
 
#verification 
t1= time.perf_counter()
for user in rserver.keys(): 
    mdp= rserver.get(user)
    mdp_hash= rhashage.get(user)
    nonce= rnonce.get(user)
    
    if not aes256.decrypAES(mdp, mdp_hash, nonce): 
        sys.exit()
      
t2= time.perf_counter()

f.write("aes:  %s\n" % (str(t2-t1)))
f.close()




