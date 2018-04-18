import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
#sys.path.insert(0, "/path/to/your/package_or_module")

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

manager = Manager(app)

if __name__ == "__main__":
    manager.run()