import os
import json
import argparse

def delete(deployment_name):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment_name", help="Name of the deployment")
    args = parser.parse_args()
    delete(args.deployment_name)
