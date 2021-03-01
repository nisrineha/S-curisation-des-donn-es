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

#def salt(): 
#    return bcrypt.gensalt()

def fun_bcrypt(mdp): 
    mdp_hash= bcrypt.hashpw(mdp.encode(), salt= bcrypt.gensalt() )
    return mdp_hash.decode('utf8')

def VerifierMdp(mdp, mdp_hash):     
    return bcrypt.checkpw(mdp.encode('utf8'), mdp_hash.encode('utf8'))


    


















