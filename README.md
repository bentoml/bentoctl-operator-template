# BentoML deployment operator template
Use this template as starting point for creating your own operators to carry out deployments.

## About

The file structure of an operator should be similar to this. Lets look at the most important pieces.
```
.
├── my_operator                #1 - the operator module
│   ├── __init__.py
│   ├── deploy.py
│   ├── describe.py
│   ├── update.py
│   └── delete.py
├── deploy                     #2 - python scripts to do operations
├── describe   
├── update   
├── delete   
├── deployment_config.json     #3 - sample config for the operator
├── operator_config.py         #4 - basic config for the operator
└── README.md
```
#1 [my_operator](./my_operator) - This module exposes the `deploy()`, `describe()`, `update()` and `delete()` functions that actually do these operations.

> Note: A good convention to use for naming operators is appending the module name with `bentoctl_`. This is to
> avoid namespace clashes with other python modules when bentoctl loads the operator. Eg `bentoctl_lambda` for the 
> lambda operator module.

#2 Python Script in the root dir - these can be called as scripts to carry out the operations
eg: running `./deploy path/to/bento iristestdeployment deployment_config.json` will do the deployment operation.

#3 [deployment_config.json](./deployment_config.json) - the sample config for operators

#4 [operator_config.py](./operator_config.py) - this contains the basic properties of the operator. This is accessed by the deployment tool. This container the operator name, the operator schema and the optional operator module path.

eg: lets see the sample operator_config file
```
OPERATOR_NAME = 'bentoml_template'

OPERATOR_MODULE_DIR= "my_operator"

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
2. Update the `OPERATOR_NAME` and `OPERATOR_SCHEMA` in the `__init__.py` file
3. Update the deployment functions in each file `deploy.py`, `update.py`, `describe.py` and `delete.py`
