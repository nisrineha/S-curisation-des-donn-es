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

def salt(): 
    salt = ''.join(random.choice(string.ascii_lowercase) for i in range(32)) 
    return salt

def fun_sha265_sels( mdp, salt):
    
    mdp_hash= hashlib.sha256(salt_global.encode() + mdp.encode()+ salt.encode()).hexdigest() 
    return mdp_hash


