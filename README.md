# BentoML Deployment Operator Template
Use this template as starting point for creating your own operators to carry out deployments with [bentoctl](https://github.com/bentoml/bentoctl) to a platform of your choice. For reference, see successful examples of [Official Operators](#official-operators).

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
1. [my_operator](./my_operator) - This module exposes the `deploy()`, `describe()`, `update()`, and `delete()` functions that do the key operations with the platform of choice. Read more about what each function should do in [Operator Functions](#operator-functions).

2. Python scripts in the root directory - They are `deploy`, `describe`, `update`, and `delete`. They can be called as scripts to carry out the operations from your terminal.
```bash
$ ./deploy path/to/bento iristestdeployment deployment_config.json # deploys given bento to the cloud with the provided deployment configuration
```

3. [deployment_config.json](./deployment_config.json) - This is used as Deployment Configuration when working with the cloud. It should provide a dictionary of attributes like `cpu`, `memory`, `dyno_count`, or anything else that can be used to setup a cloud environment suitable to your Bento's needs. Reference your chosen platform for the configuration it requires.

4. [operator_config.py](./operator_config.py) - This contains the basic properties for the template to work as an opperator. The properties are accessed by bentoctl. Contains the operator name (eg. heroku, aws-lambda, etc.), the operator schema and the optional operator module path.

Let's see the sample `operator_config.py` file
```
OPERATOR_NAME = 'bentoml_template' # named used to define this operator in bentoctl

OPERATOR_MODULE= "my_operator" # path to the module my_operator

# bentoctl uses Cerberus to validate the input of your `deploymen_config.json` before using the settings. The following is an example of the schema validation.
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

Read more about Cerberus here https://docs.python-cerberus.org/en/stable/.

## Setup

This is a template repository for bentoctl. To create a new deployment operator:

1. Click "Use this template" button to start a new repository
2. Update the `OPERATOR_NAME`, `OPERATOR_MODULE` and `OPERATOR_SCHEMA` in the `operator_config.py` to register the new operator `bentoctl operators add name-of-your-operator`
3. Update the deployment functions in each file `deploy.py`, `update.py`, `describe.py` and `delete.py`


## Official Operators

This is the list of operators that are currently officially supported for bentoctl. 

1. [Heroku Deployment Tool](https://github.com/bentoml/heroku-deploy)
2. [Google Cloud Run Deployment Tool](https://github.com/bentoml/google-cloud-run-deploy)

## Operator Functions

There are different ways one can deploy bento to a plaform, but the general tasks needed to manage bento online can be divided into four categories: deploy, describe, update, delete. At the basic level, the operator must run bash commands associated with pushing a Docker container to the platform.

1. `deploy.py` must run commands associatiated with pushing the bento container to the platform

For example:  Heroku
```bash
$ heroku container:push web --app test-script 
$ heroku contiainer:release web --app test-script
```

