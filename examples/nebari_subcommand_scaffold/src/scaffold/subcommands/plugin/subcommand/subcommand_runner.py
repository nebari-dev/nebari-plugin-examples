import os

from camel_converter import to_snake
from cookiecutter.main import cookiecutter

def run(name: str, out: str, force: bool):
    project_name = to_snake(name.replace('-', '_'))
    print(f"Attempting to generate Nebari subcommand scaffold {name}...")

    templates_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
    out_path = os.path.abspath(out)

    cookiecutter(
        template = templates_path,
        overwrite_if_exists = force,
        output_dir = out_path,
        no_input = True,
        extra_context = {
            'project_name': project_name
        }
    )

    # https://github.com/cookiecutter/cookiecutter/issues/1601
    strip_extension(out_path, '.j2')

    print(f'Successfully generated Nebari {project_name} subcommand plugin scaffold to {out_path}.')

def strip_extension(p: str, ext: str):
    for path, _, files in os.walk(p):
        for f in files:
            if f.endswith(ext):
                old_name = os.path.join(path, f)
                new_name = os.path.join(path, f.strip(ext))
                os.rename(old_name, new_name)
