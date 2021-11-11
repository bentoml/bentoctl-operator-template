#!/usr/bin/env python3

import argparse
import json
import os

import my_operator as myop

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bento_bundle_path", help="Path to Bento bundle")
    parser.add_argument("deployment_name", help="Name of the deployment")
    parser.add_argument(
        "config_path",
        help="Configuration file for the deployment",
        default=os.path.join(os.getcwd(), "deployment_config.json"),
        nargs="?",
    )
    args = parser.parse_args()
    with open(args.config_path, "r") as file:
        deployment_spec = json.loads(file.read())

    myop.deploy(args.bento_bundle_path, args.deployment_name, deployment_spec)
