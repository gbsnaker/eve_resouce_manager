log_schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        'unique': True,
    },
    # create version
    'path': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
}

log = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'log',

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

    #'internal_resource': True
    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': log_schema
}