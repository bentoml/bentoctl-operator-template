import argparse
import json
import os

import my_operator as myop

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "deployment_spec_json",
        help="Deployment spec file for the deployment",
        default=os.path.join(os.getcwd(), "deployment_config.json"),
    )
    args = parser.parse_args()
    with open(args.deployment_spec_json, "r") as file:
        deployment_spec = json.loads(file.read())
    myop.delete(args.deployment_name, deployment_spec)
