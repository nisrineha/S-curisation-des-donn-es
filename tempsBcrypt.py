# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:18:13 2021

@author: Nisrine
"""
import redis 
import string
import random
import bcryct2
import time
import sys 
#Verification 10000 pour sha


rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rhashage= redis.StrictRedis(host="localhost", port=6379, db=4, decode_responses=True)
rserver.flushdb()
rhashage.flushdb()
#remplir une base en plain
f = open("10000_8.txt", "a")
#1 cara
#rnd_lists= random.choices(string.ascii_lowercase, k = 1000)
#8 cara
rnd_lists=[]
for i in range(10000):  
    listss=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    rnd_lists.append(listss)

for i in range(len(rnd_lists)): 
    rserver.set(i, rnd_lists[i])

#hashage
for user in rserver.keys(): 
    mdp= rserver.get(user)
    rhashage.set(user, bcryct2.fun_bcrypt(mdp))

#verification 
t1= time.perf_counter()
for user in rserver.keys(): 
    mdp= rserver.get(user)
    mdp_hash= rhashage.get(user)
    
    if not bcryct2.VerifierMdp(mdp, mdp_hash): 
        sys.exit()
        
t2= time.perf_counter()

f.write("bcrypt:  %s\n" % (str(t2-t1)))
f.close()




