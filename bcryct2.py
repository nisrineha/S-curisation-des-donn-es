# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:40:23 2021

@author: Nisrine
"""
import bcrypt
import redis
# Definer les dbs
rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)

#fonction cryptage
def fun_bcrypt(mdp): 
    mdp_hash= bcrypt.hashpw(mdp.encode(), salt= bcrypt.gensalt() )
    return mdp_hash.decode('utf8')

#fonction de verification
def VerifierMdp(mdp, mdp_hash):     
    return bcrypt.checkpw(mdp.encode('utf8'), mdp_hash.encode('utf8'))


    


















