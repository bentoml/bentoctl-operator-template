import os
import json
import argparse

def update(deployment_name, deployment_config, bento_bundle_path=None):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "deployment_spec_json",
        help="Deployment spec file",
        default=os.path.join(os.getcwd(), "deployment_spec.json")
    )
    parser.add_argument(
        "bento_bundle_path",
        help="Path to Bento bundle",
        default=None
    )
    args = parser.parse_args()
    with open(args.config_json, 'r') as file:
        deployment_spec = json.loads(file.read())
    update(args.deployment_name, deployment_spec, args.bento_bundle_path)
