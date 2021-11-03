from .deploy import deploy
from .update import update
from .delete import delete
from .describe import describe


# help message
OPERATOR_NAME = 'bentoml_template'

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
