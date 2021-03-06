import os

def create_deployable(bento_path: str, destination_dir, bento_metadata:dict, overwrite_deployable=True) -> str:
    """
    Create deployable and return path to the deployable, dockerfile, docker context path and additional build args
    """
    deployable_path = "deployable"
    dockerfile_path = os.path.join(deployable_path, "Dockerfile")
    docker_context_path = deployable_path
    additional_build_args = []
    return deployable_path, dockerfile_path, docker_context_path, additional_build_args
