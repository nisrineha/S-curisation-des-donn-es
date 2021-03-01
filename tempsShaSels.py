# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:08:59 2021

@author: Nisrine
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:38:16 2021
@author: Nisrine
"""
import redis 
import string
import random
import sha3
import time
import sys 
#Verification 10000 pour sha


rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)
rhashage= redis.StrictRedis(host="localhost", port=6379, db=4, decode_responses=True)
rserver.flushdb()
rsalt.flushdb()
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
    user_salt= sha3.salt()
    rhashage.set(user, sha3.fun_sha265_sels(mdp, user_salt))
    rsalt.set(user, user_salt)

#verification 
t1= time.perf_counter()
for user in rserver.keys(): 
    mdp= rserver.get(user)
    user_salt= rsalt.get(user)
    
    if sha3.fun_sha265_sels(mdp, user_salt) not in rhashage.get(user): 
        sys.exit()
        
t2= time.perf_counter()

f.write("sha+sel+user:  %s\n" % (str(t2-t1)))
f.close()




