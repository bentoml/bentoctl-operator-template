import os
import json
import argparse

def update(deployment_name, deployment_config, bento_bundle_path=None):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "config_json",
        help="Configuration file for the deployment",
        default=os.path.join(os.getcwd(), "deployment_config.json")
    )
    parser.add_argument(
        "bento_bundle_path",
        help="Path to Bento bundle",
        default=None
    )
    args = parser.parse_args()
    with open(args.config_json, 'r') as file:
        deployment_config = json.loads(file.read())
    update(args.deployment_name, deployment_config, args.bento_bundle_path)
