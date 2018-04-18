# coding: utf-8


envs_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        'unique': True,
    },
    'version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    # 'role': {
    #     'type': 'list',
    #     'allowed': ["author", "contributor", "copy"],
    # },
    # An embedded 'strongly-typed' dictionary.
    'creater': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
                        'data_relation': {
                'resource': 'people',
                'field': '_id',
                'embeddable': True
            }
        }
    },
    'items': {
        'type': 'list',
        'schema': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'items',
                'field': '_id',
                'embeddable': True
            }
        }
    } ,
    # 'item': {
    #     'type': 'dict',
    #     'schema': {
    #         'name': {'type': 'string'},
    #         'version': {'type': 'string'}
    #     },
    # },
    'stroy': {
        'type': 'boolean',
        'default': False,
    },
}


envs = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': '环境',

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

    'schema': envs_schema
}


