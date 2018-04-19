# coding: utf-8
import bcrypt
from werkzeug.security import check_password_hash
from hashlib import sha1
import hmac
from flask import request, abort


from eve.auth import TokenAuth
from eve.auth import HMACAuth
from flask import current_app as app
from eve.auth import BasicAuth

from backend.commons.common import verify_password

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        print "incoming"
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'mail': username})

        return user and \
            verify_password(password, user['hash_password'])

class BCryptAuthPost(BasicAuth):
    def check_auth(self,username, password, allowed_roles, resource, method):
        username = request.json.get('username') or request.json.get('mail')
        password = request.json.get('password')
        if not username or not password:
            abort(404)

        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'mail': username})

        return user and \
            verify_password(password, user['hash_password'])
