from backend.Resources.Envs import envs
from backend.Resources.Items import items
from backend.Resources.Accounts import accounts
from backend.Resources.People import people
from backend.Resources.log import log
# Let's just use the local mongod instance. Edit as needed.
# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'envmanager'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
ESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
## individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# RENDERERS = [
#     'eve.render.JSONRenderer',
#     'eve.render.XMLRenderer'
# ]
#cros
#X_DOMAINS_RE = ['^http://sub-\d{3}\.example\.com$']

#jsonp
#JSON_ARGUMENT = 'callback'

#docker run -p 8888:8080 swaggerapi/swagger-ui

# X_DOMAINS = ['http://localhost:8000',  # The domain where Swagger UI is running
#              'http://editor.swagger.io',
#              'http://petstore.swagger.io']
X_DOMAINS = ['http://127.0.0.1:8888']
X_HEADERS = ['Content-Type', 'If-Match']  # Needed for the "Try it out" buttons


DOMAIN = {
        'envs': envs,
        'items': items,
        'accounts': accounts,
        'people': people,
        # 'log': log
        }