# coding: utf-8


item_schema = {
    #apps-manage-service
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        'unique': True,
    },
    #create version
    'version': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 120,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
    },
    'jvmruntime': {
        'type': 'dict',
        'schema': {
            'mainclass': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 120,
                'required': True
            },
            'jvm_port': {
                'type': 'integer',
                'required': True
                },
            'service_port': {
                'type': 'list',
                'required': True
            },
            'java_version': {
                'type':'string',
                'allowed': ['jdk1.8', 'jdk1.7']
            },
            'java_options': {
                'type':'string',
                'minlength': 1,
                'maxlength': 300
            },
        },
    },
    'maven_env': {
        'type': 'string',
        'allowed': ['mvn3.3-jdk7', 'mvn2.2-jdk7','mvn3.3-jdk8']
    },
    'wirte_service_started': {
        'type': 'boolean',
        'default': False,
    },
    'gulp': {
        'type': 'boolean',
        'default': False,
    },
    'have_gray_nginx': {
        'type': 'boolean',
        'default': True,
    },
    # 'logs': {
    #     'type': 'list',
    #     'schema': {
    #         'type': 'objectid',
    #         'data_relation': {
    #             'resource': 'log',
    #             'embeddable': True,
    #             'field': '_id'
    #         }
    #     }
    # },
    'log': {
      'type' : 'list',
       'schema': {
           'type': 'dict',
           'schema': {
               'name': { 'type': 'string' },
               'path': { 'type': 'string' }
           }
       }
    },
    'required_dns': {
        'type': 'list',
        'schema': {
            'type': 'string'
        }
    },
    'required_middlewares': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'name': {
                    'type': 'string'
                },
                'decrpitions': {
                    'type': 'string'
                },
                'ports_list': {
                    'type': 'list',
                    'schema' : {
                        'type': 'dict',
                         'schema': {
                             'name': {'type': 'string'},
                             'port': {'type': 'string'},

                         }
                    }
                }
            }
        },
    },
    # 'others': {
    #     'type': 'list',
    #     'schema': {
    #         'name': {
    #             'type': 'string'
    #         },
    #         'decrpitions': {
    #             'type': 'string'
    #         }
    #     }
    # },
    #item creater
    # 'author': {
    #      'type': 'dict',
    #      'schema': {
    #          '_id': {'type': 'objectid'},
    #          '_version': {'type': 'integer'}
    #      },
    #      'data_relation': {
    #          'resource': 'users',
    #          'field': '_id',
    #          'embeddable': True,
    #          'version': True,
    #      },
    #  },
}


items = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': '应用',

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

    'schema': item_schema
}
