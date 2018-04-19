from flask import jsonify, abort,make_response
from flask import current_app as app 

from Accounts import accounts_schema
from backend.auths.allauths import BCryptAuth
from backend.commons.common import verify_password, hash_password
from backend.commons.abortext import abort_json,abrot_json_ok

login = {
    'datasource': {
        'source': 'accounts',
        'filter': {'mail': 1}
        },
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'login',
    'url': 'auth/login',
    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'mail'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': accounts_schema
}

def pre_login_post_callback(request):
    print('A login on the accounts endpoint has just been received!')
    # print type(request.json)
    # print request.json
    mail = request.json.get('mail')
    password = request.json.get('password')
    remember = request.json.get('remember')
    if not mail or not password:
        abort_json("check your input", 400)

    request.json['hash_password'] = hash_password(request.json['password'])
    del request.json['password']

    accounts = app.data.driver.db['accounts']
    user = accounts.find_one({'mail': mail})
    if not verify_password(password,user['hash_password']):
        #print request.json['hash_password']

        abort_json("password is invlid !", 500)

    #print user['_id']
    if user['remember'] != remember:
        #user['remember'] = remember
        accounts.update(
            {'_id': user['_id']},
            {
                '$set': {
                    'remember': remember
                }
            }
        )

    #abrot_json_ok(message="ok", status="success")
    #abort(make_response(jsonify({"status": "ok", "message": ""})), 201)
    #return jsonfiy(message=message)
    

