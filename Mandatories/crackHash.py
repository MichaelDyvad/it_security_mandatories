import hashlib
from msilib.schema import File
from passlib.hash import sha512_crypt
import random

encoded = "$6$penguins$eP.EvNiF2A.MmRVWNgGj5WSXKK8DAf7oeK8/kkbollee.F0T4KAy.QEgNAX.6wLQY1XHmSID/5VkeFiEaSA2b0"

#Den encoded kode er 479
for i in range(10000):
    guess1 = random.randint(0,9)
    guess2 = random.randint(0,9)
    guess3 = random.randint(0,9)
    ar = str(guess1) + str(guess2) + str(guess3)
    hash2 = sha512_crypt.using(salt = "penguins", rounds=5000).hash(ar)
    print(ar)
    if(hash2 == encoded):
        print("This is the hashed code : ", ar)
        break
