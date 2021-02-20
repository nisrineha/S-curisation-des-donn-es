# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:40:23 2021

@author: Nisrine
"""
import bcrypt
import redis

#bcrypt

rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)

def fun_bcrypt(mdp): 
    salt = bcrypt.gensalt()
    mdp_hash= bcrypt.hashpw(mdp.encode(),salt )
    return mdp_hash, salt


'''
for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i]))   
for i in range(len(rserver.keys())):
    salt = bcrypt.gensalt(12)
    
    mdp_hash = rserver.get(rserver.keys()[i])
    rserver.set(rserver.keys()[i], bcrypt.hashpw(mdp_hash.encode(),bcrypt.gensalt(12) ))

    rsalt.set(rserver.keys()[i], salt)

for i in range(len(rserver.keys())):
    
    mdp_hash = rserver.get(rserver.keys()[i])
    rserver.keys()[i]
    fun_bcrypt(rserver.keys()[i], mdp_hash)
    
    
for i in range(len(rsalt.keys())):
   print(rsalt.keys()[i], rsalt.get(rsalt.keys()[i]))   
''' 


























