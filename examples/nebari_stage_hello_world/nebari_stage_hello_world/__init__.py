import contextlib
import os
from typing import Dict, Any

from nebari.hookspecs import hookimpl, NebariStage


class HelloWorldStage(NebariStage):
    name = "hello_world"
    priority = 100

    def render(self):
        return {
            "hello_world.txt": "File that says hello world"
        }

    @contextlib.contextmanager
    def deploy(self, stage_outputs: Dict[str, Dict[str, Any]]):
        print("I ran deploy")
        # set environment variables for stages that run after
        os.environ['HELLO'] = 'WORLD'
        # set output state for future stages to use
        stage_outputs[self.name] = {'hello': 'world'}
        yield
        # cleanup after deployment (rarely needed)
        os.environ.pop('HELLO')

    def check(self, stage_outputs: Dict[str, Dict[str, Any]]):
        if 'HELLO' not in os.environ:
            raise ValueError('stage did not deploy successfully since HELLO environment variable not set')

    @contextlib.contextmanager
    def destroy(self, stage_outputs: Dict[str, Dict[str, Any]], status: Dict[str, bool]):
        print('faking to destroy things for hello world stage')
        yield


@hookimpl
def nebari_stage():
    return [HelloWorldStage]
