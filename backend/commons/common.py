from passlib.apps import custom_app_context as pwd_context


def verify_password(password,password_hash):
    return pwd_context.verify(password, password_hash)


def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash