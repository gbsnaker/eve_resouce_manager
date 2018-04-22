#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-20 下午6:08
# @Author  : gbsnaker
# @Site    : 
# @File    : create_token.py
# @Software: PyCharm

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask import current_app as app
import jwt


def generate_auth_token2(expiration=600, mail=""):
    s = Serializer(app.config['JWT_SECRET'], expires_in=expiration)
    return s.dumps({'mail': mail})

def generate_auth_token(expiration=600, mail=""):
    s = Serializer(app.config['JWT_SECRET'], expires_in=expiration)
    return s.dumps({'mail': mail})