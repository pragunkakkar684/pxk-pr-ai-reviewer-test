import hashlib

def eval_user_input(user_code):
    return eval(user_code)  # ❌ dangerous

def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()  # ❌ insecure hashing
