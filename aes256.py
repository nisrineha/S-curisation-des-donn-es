import redis
import bcrypt
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import base64 
#bcrypt
rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt = redis.StrictRedis(host="localhost", port=6379, db=1, decode_responses=True)
rsalt_global = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)

key = get_random_bytes(32)
rsalt_global.set('key', base64.b64encode(key).decode('utf-8'))
cipher = AES.new(key, AES.MODE_CTR)

def fun_aes(mdp):
   
    salt = bcrypt.gensalt(12)
    mdp_hash= bcrypt.hashpw(mdp.encode('utf-8'),salt)
    padding = cipher.encrypt(pad(mdp_hash,16))
    mdp_hash= base64.b64encode(padding).decode('utf-8')
    
    return mdp_hash, salt
 
'''
for i in range(len(rserver.keys())):
    salt = bcrypt.gensalt(12)
    #mdp_hash = rserver.get(rserver.keys()[i])
    mdp_hash= bcrypt.hashpw(rserver.get(rserver.keys()[i]).encode('utf-8'),bcrypt.gensalt(12))
    b = cipher.encrypt(pad(mdp_hash,16))
    ct= base64.b64encode(b).decode('utf-8')
    rserver.append(rserver.keys()[i], ct) 

    rsalt.set(rserver.keys()[i], salt)
for i in range(len(rserver.keys())):
    
    mdp_hash = rserver.get(rserver.keys()[i])

    fun_aes(rserver.keys()[i], mdp_hash)
    

for i in range(len(rsalt.keys())):
   print(rsalt.keys()[i], rsalt.get(rsalt.keys()[i]))   
   
for i in range(len(rserver.keys())):
   print(rserver.keys()[i], rserver.get(rserver.keys()[i])) 
'''