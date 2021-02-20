# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:34:11 2021

@author: Nisrine
"""
import redis
import string
import hashlib
import random

#info log admin= tp mdp n

rserver = redis.StrictRedis(host="localhost", port=6379, db=0,  decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)
rsalt_global = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)
#rsalt.flushdb()

### SHA-256

def fun_sha256(mdp):
    mdp_hash= hashlib.sha256(mdp.encode()).hexdigest()
    return mdp_hash

###SHA+ Sel
salt_global = 'SelGlobal'
rsalt_global.set('SelGlobal', salt_global)

def fun_sha256_selglobal(mdp):
    mdp_hash= hashlib.sha256(salt_global.encode() + mdp.encode()).hexdigest()
    return mdp_hash

###SHA+Sel+Seluser

salt_global= rsalt_global.get('SelGlobal')

def fun_sha265_sels(mdp):
    salt = ''.join(random.choice(string.ascii_lowercase) for i in range(32)) 
    mdp_hash= hashlib.sha256(salt_global.encode() + mdp.encode()+ salt.encode()).hexdigest() 
    return mdp_hash, salt




'''  
 
for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i]))   
 
   
for i in range(len(rserver.keys())):
    mdp_hash = rserver.get(rserver.keys()[i])
    rserver.set(rserver.keys()[i], fun_sha256(mdp_hash) )
    
for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i]))  

for i in range(len(rserver.keys())):
    
    mdp_hash = rserver.get(rserver.keys()[i])
    rserver.set(rserver.keys()[i], fun_sha256_selglobal(mdp_hash))


def encrypt_SHA(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


for i in range(len(rserver.keys())):
    
    mdp_hash = rserver.get(rserver.keys()[i])
    rserver.keys()[i]
    fun_sha265_sels(rserver.keys()[i], mdp_hash)

for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i]))   

for i in range(len(rsalt.keys())):
   print(rsalt.keys()[i], rsalt.get(rsalt.keys()[i]))

   
for i in range(len(rsalt.keys())):
   print(rsalt.keys()[i], rsalt.get(rsalt.keys()[i]))

for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i]))
   

'''  
   
   
   
   
   
   
   
   
   
   
   
   