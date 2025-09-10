#first lesson ( how to hash a word in md5 format )

#for Example : first , We have to import the module that responsible for hashing operation such as ( Hashlib ) module 

#from hashlib import *

# for example word ( Test ) let's hash it using Md5 Format :

#md5('Test'.encode()).hexdigest()

# the outcomes will be '0cbc6611f5540bd0809a388dc95a615b'

#########################################################
# Let's create a quick script that takes the info and the words from the user in order to be hashed in Md5 format 
from hashlib import *

user = str(input('Kindly enter your wanted password :' ))

z = md5(user.encode()).hexdigest()

print(z)    
