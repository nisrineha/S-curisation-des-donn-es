# -*- coding: utf-8 -*-
"""
@author: Nisrine
"""
# library 
import sha3
import redis
import bcryct2
import aes256
rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)
rsalt_global = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)
rnonce = redis.StrictRedis(host="localhost", port=6379, db=3, decode_responses=True)
#rserver.flushdb()

"""
interface textuelle basique : 
 * Login &mdp*2 
 * Données stockées sur la bd
 * unicité de login, mm mdp 
 * admin user= tp
"""
#********Bienvenue d'un utilisateur 
def welcome(): 
    print('welcome')
    choix = input('do you have an account? (y/n) : ')
    
    if choix== 'y':
        print('Connexion')
        connexion()
    elif choix=='n': 
        print('inscription')
        inscription()
    else: 
        print('invalid entry')
        c2= input('do you want to try again? (y/n) :  ')
        if c2== 'y':     
            welcome()
        else:
            print('goodbye')
        
############Inscription
def inscription():
    log = input('Username : ')
    mdp = input('Password : ')
    cRmdp = input('Confirm Password : ')
    
    if log in rserver.keys(): 
        print('account already exists, please connect')
        welcome()
    else: 
        if mdp == cRmdp:
                print('Welcome')
                rserver.set(log, mdp)
                
        else:
                print("Password unmatch")
                c2= input('do you want to try again? (y/n) :  ')
                if c2== 'y':     
                    inscription()
                else:
                    print('goodbye')
                
################login         
def connexion():
    log= input('Username : ')
    mdp= input('Password : ')
   
    if log not in rserver.keys():
        print('invalid user') 
        c2= input('do you want to try again? (y/n) :  ')
        if c2== 'y':     
            connexion()
        else:
            print('goodbye')
    else:   
    
        if  mdp in rserver.get(log):
            if log=='tp': 
                print('welcome admin :), here is our users : ')
                for i in range(len(rserver.keys())):
                    print(rserver.keys()[i], rserver.get(rserver.keys()[i]))
            else: 
                print('welcome user')
        else: 
            print('wrong password')
            c2= input('do you want to try again? (y/n) :  ')
            if c2== 'y':     
                connexion()
            else:
                print('goodbye')
  
  
welcome()


 