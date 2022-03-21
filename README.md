# BentoML deployment operator template
Use this template as starting point for creating your own operators to carry out deployments.

## About
This is a template for a Bentoctl deployment operator.

The file structure of an operator should be similar to this. Lets look at the most important pieces.
```
.
├── my_operator                #1 - the operator module
│   ├── __init__.py
│   ├── create_deployable.py
│   └── generate.py
├── operator_config.py         #2 - basic config for the operator
└── README.md
```
#1 [my_operator](./my_operator) - This module exposes the `generate()`, and `create_deployable()` functions

> Note: A good convention to use for naming operators is appending the module name with `bentoctl_`. This is to
> avoid namespace clashes with other python modules when bentoctl loads the operator. Eg `bentoctl_lambda` for the
> lambda operator module.

#2 [operator_config.py](./operator_config.py) - this contains the basic properties of the operator. This is accessed by the deployment tool. This container the operator name, the operator schema and the optional operator module path.

eg: lets see the sample operator_config file
```
OPERATOR_NAME = 'bentoml_template'

OPERATOR_MODULE_DIR= "my_operator"

OPERATOR_DEFAULT_TEMPLATE = 'terraform'

OPERATOR_AVAILABLE_TEMPLATES = ['terraform', 'kubernetes']

# BentoML deployment tool use Cerberus to validate the input. The following is an example of the schema validation.
OPERATOR_SCHEMA = {
    "project_name": {"type": "string"},
    "system_requirements": {
        "type": "dict",
        "allow_unknown": False,
        "require_all": True,
        "schema": {
            "cpu": {"type": "integer", "min": 1},
            "memory": {"type": "integer", "min": 100},
        },
    },
}
```

The `OPERATOR_SCHEMA` specfies the schema and data type for the configurable options. Bentoctl uses [Cerberus](https://docs.python-cerberus.org/en/stable/) for specifying and validation the schema for an operators configurable
options. Reffer to the [validation rules](https://docs.python-cerberus.org/en/stable/validation-rules.html) for rules
that can be applyed.

## Setup

This is a template repository for BentoML dpeloyment operator. To Create a new deployment operator:

1. Click "Use this template" button to start a new repository
2. Update the `OPERATOR_NAME`, `OPERATOR_SCHEMA` `OPERATOR_DEFAULT_TEMPLATE` in the `__init__.py` file

