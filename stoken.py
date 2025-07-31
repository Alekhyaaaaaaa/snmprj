from itsdangerous import URLSafeTimedSerializer
salt='otpverify'
def entoken(data):
    serializer=URLSafeTimedSerializer('Akhi0703')
    return serializer.dumps(data,salt=salt)
def dntoken(data):
    '''Function to decrypt encrypted token'''
    serializer=URLSafeTimedSerializer('Akhi0703')
    return serializer.loads(data,salt=salt)