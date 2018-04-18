import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
#sys.path.insert(0, "/path/to/your/package_or_module")

from flask import jsonify, abort
from flask_script import Manager
from eve import Eve
#from eve_swagger import swagger, add_documentation


if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

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

def pre_accounts_post_callback(request):
    print('A post request on the accounts endpoint has just been received!')
    print request.json
    #data = request.json[0]

    # mail = data.get('mail')
    # print mail
    # password = data.get('password')
    # verify = data.get('verify')
    # name = data.get('name')
    #
    # if password != verify:
    #     abort(404)
    tmp_list = []
    for item in request.json:
        del item['verify']
        item['hash_password'] = item['password']
        del item['password']
        tmp_list.append(item)

app.on_pre_GET += pre_get_callback
app.on_pre_GET_accounts += pre_accounts_get_callback

app.on_pre_POST_accounts += pre_accounts_post_callback

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






manager = Manager(app)

if __name__ == "__main__":
    manager.run()