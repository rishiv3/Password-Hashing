import uuid
import hashlib

def hashText(text):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + text.encode()).hexdigest() + ':' + salt
    
def checkHashedText(hashedText, providedText):
    _hashedText, salt = hashedText.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + providedText.encode()).hexdigest()
    
#testing -     
print(hashText('password')) #hashed password
print(checkHashedText(hashText('password'),'password')) #checking password - returns true if matched
