import redis
from Crypto.Cipher import AES
import base64 

# definir les dbs
rserver = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
rsalt_global = redis.StrictRedis(host="localhost", port=6379, db=2, decode_responses=True)
rnonce = redis.StrictRedis(host="localhost", port=6379, db=3, decode_responses=True)
# definir la clé 
key = b"This_key_for_demo_purposes_only!"
rsalt_global.set('key', key)

# fonction cryptage
def fun_aes(mdp):
    cipher = AES.new(key, AES.MODE_CTR)
    mdp_cipher = cipher.encrypt( mdp.encode())
    nonce= base64.b64encode(cipher.nonce).decode('utf-8')
    mdp_aes= base64.b64encode(mdp_cipher).decode('utf-8')
    return mdp_aes , nonce

#fonction decryptage
def decrypAES(mdp, mdp_hash, nonce):
    
    mdp_decode= base64.b64decode(mdp_hash)
    nonce= base64.b64decode(nonce)
    
    cipher= AES.new(key, AES.MODE_CTR, nonce= nonce)
    mdp_decrypt= cipher.decrypt(mdp_decode)    
    return mdp_decrypt== mdp.encode()
    
    
