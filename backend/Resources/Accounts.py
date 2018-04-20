# coding: utf-8
#from flask import current_app as app
from passlib.apps import custom_app_context as pwd_context
from backend.commons.abortext import abort_json
from backend.commons.common import verify_password, hash_password
from redis import StrictRedis
from backend.commons.create_token import generate_auth_token

accounts_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
    },
    'mail': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'remember': {
        'type': 'boolean',
        'default': False
    },
    'hash_password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["admin", "normal"],
    },
}

accounts = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'accounts',
    'url': 'auth/register',
    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': accounts_schema
}

def pre_accounts_post_callback(request):
    print('A post request on the accounts endpoint has just been received!')
    print type(request.json)
    print request.json
    mail = request.json.get('mail')
    password = request.json.get('password')
    confirm = request.json.get('confirm')

    if not mail or not password or not confirm:
        abort_json("check your input", 400)

    if password != confirm:
        abort_json("password must be match!", 500)

    del request.json['confirm']
    #print hash_password("123")

    request.json['hash_password'] = hash_password(request.json['password'])
    del request.json['password']


    token = generate_auth_token(mail)
    redis = StrictRedis()
    redis.set(mail=token)


