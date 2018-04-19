import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
#sys.path.insert(0, "/path/to/your/package_or_module")

from flask import jsonify, abort, request
from flask_script import Manager
from eve import Eve
from eve.auth import BasicAuth

from backend.Resources.Accounts import pre_accounts_post_callback
from backend.Resources.login import pre_login_post_callback

from backend.auths.bcryptauth import BCryptAuth,BCryptAuthPost
from backend.commons.common import hash_password, verify_password
#from eve_swagger import swagger, add_documentation


if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'


class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin@tom.com' and password == 'tom.1234'



#app = Eve(auth=BCryptAuth)
#app = Eve(auth=BCryptAuth)
#app = Eve(auth=BCryptAuthPost)
app = Eve()
#app.register_blueprint(swagger)
# required. See http://swagger.io/specification/#infoObject for details.
# app.config['SWAGGER_INFO'] = {
#     'title': 'My Supercool API',
#     'version': '1.0',
#     'description': 'an API description',
#     'termsOfService': 'my terms of service',
#     'contact': {
#         'name': 'evedemo',
#         'url': 'https://github.com/gbsnaker/evedemo'
#     },
#     'license': {
#         'name': 'BSD',
#         'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
#     },
#     'schemes': ['http', 'https'],
# }

# optional. Will use flask.request.host if missing.
#app.config['SWAGGER_HOST'] = '127.0.0.1'
#/api-docs
# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
# add_documentation({'paths': {'/status': {'get': {'parameters': [
#     {
#         'in': 'query',
#         'name': 'foobar',
#         'required': False,
#         'description': 'special query parameter',
#         'type': 'string'
#     }]
# }}}})

# configure your app
def pre_get_callback(resource, request, lookup):
    print('A GET request on the "%s" endpoint has just been received!' % resource)
def pre_accounts_get_callback(request, lookup):
    print('2 A GET request on the accounts endpoint has just been received!')


app.on_pre_GET += pre_get_callback
app.on_pre_GET_accounts += pre_accounts_get_callback

app.on_pre_POST_accounts += pre_accounts_post_callback
app.on_pre_POST_login += pre_login_post_callback
# def post_get_callback(resource, request, payload):
#     print "all get callback"
#
#
# def post_accounts_get_callback(request, payload):
#     print "account"
#     print request.json
#     print payload
#
# app.on_post_GET += post_get_callback
# app.on_post_GET_accounts  += post_accounts_get_callback



@app.route('/auth/login', methods=["POST"])
def login():
    username = request.json.get('username') or request.json.get('mail')
    password = request.json.get('password')

    if not username or not password:
        abort(404)

    accounts = app.data.driver.db['accounts']
    user = accounts.find_one({'mail': username})
    print user
    if not user:
        status = "error"
        message = "user not exist"
        return  jsonify(status=status,messag=message)

    if not verify_password(password, user['hash_password']):
        status = "error"
        message = "password invalid"
        return jsonify(status=status,messag=message)

    status = "success"
    message = "login ok"
    token = ""
    return jsonify(status=status,messag=message, token=token)


manager = Manager(app)

if __name__ == "__main__":
    manager.run()