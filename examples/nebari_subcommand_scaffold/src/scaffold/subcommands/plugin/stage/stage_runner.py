import os
import rich

from enum import Enum

# TODO

class StagePluginType(str, Enum):
    default = 'default'
    terraform = 'terraform'
    helm = 'helm'
    
def run(
    name: str,
    priority: int,
    out: str,
    type: StagePluginType,
):
    out_path = os.path.abspath(out)
    if type == StagePluginType.terraform:
        _terraform(name, priority, out_path)
    elif type == StagePluginType.helm:
        _helm(name, priority, out_path)
    else:
        _default(name, priority, out_path)

def _default(
    name: str,
    priority: int,
    out_path: str,
    ):
    rich.print(f"Generic Stage plugin: Name - {name}, Priority - {priority}")

def _terraform(
    name: str,
    priority: int,
    out_path: str,
    ):
    rich.print(f"Terraform Stage plugin: Name - {name}, Priority - {priority}")

def _helm(
    name: str,
    priority: int,
    out_path: str,
    ):
    rich.print(f"Helm Stage plugin: Name - {name}, Priority - {priority}")
