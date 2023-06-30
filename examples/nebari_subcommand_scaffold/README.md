# nebari-plugins

## Installation

1. Clone [nebari/extension-mechanism](https://github.com/nebari-dev/nebari/tree/extension-mechanism) and [nebari-plugin-examples](https://github.com/MetroStar/nebari-plugin-examples).

2. Install packages.
``` bash

cd nebari
pip install -e .[dev]
nebari --version # sample output: 2023.5.2.dev110+gb71cfb18
nebari --help # confirm scaffold and foobar are not in the list of available commands

cd ../nebari-plugin-examples/nebari_subcommand_scaffold
pip install -e .
pytest # 9 passing tests (as of 2023-06-29)
nebari --help # scaffold should now be in the list of available commands
nebari scaffold plugin subcommand foobar -o ../out -f # generate a subcommand type plugin named foobar in ../out/foobar and overwrite if already present

cd ../out/foobar
pip install -e .
pytest # 2 passing tests (as of 2023-06-29)
nebari --help # foobar should now be in the list of available commands
nebari foobar -n Sample # sample output: Hello, Sample

```

---
## Reference

- Nebari (dev build) - [extension-mechanism](https://github.com/nebari-dev/nebari/tree/extension-mechanism)
- Command Line - [Typer](https://typer.tiangolo.com/)
- Configuration and Schema Validation - [Pydantic](https://docs.pydantic.dev/latest/)
- Plugin Management - [Pluggy](https://pluggy.readthedocs.io/en/stable/)
