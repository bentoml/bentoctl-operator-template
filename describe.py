import os
import json
import argparse

def describe(deployment_name, deployment_config):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "config_json",
        help="Configuration file for the deployment",
        default=os.path.join(os.getcwd(), "deployment_config.json")
    )
    args = parser.parse_args()
    with open(args.config_json, 'r') as file:
        deployment_config = json.loads(file.read())
    describe(args.deployment_name, deployment_config)
