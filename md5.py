#import hashlib
#print(hashlib.md5("123456".encode()).hexdigest())

import bcrypt
print(bcrypt.hashpw("123456".encode(), bcrypt.gensalt()))
