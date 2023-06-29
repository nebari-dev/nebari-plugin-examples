import pytest

from _nebari.cli import create_cli
from typer.testing import CliRunner

runner = CliRunner()

@pytest.mark.parametrize('args, exit_code, content', [
    # --help
    (['--help'], 0, ['scaffold']),
    (['scaffold', '--help'], 0, ['plugin']),
    (['scaffold', 'plugin', '--help'], 0, ['stage', 'subcommand']),
    (['scaffold', 'plugin', 'stage', '--help'], 0, ['name', 'priority']),
    (['scaffold', 'plugin', 'subcommand', '--help'], 0, ['name']),

    # error, missing args
    (['scaffold'], 2, ['Missing command']),
    (['scaffold', 'plugin'], 2, ['Missing command']),
    (['scaffold', 'plugin', 'stage'], 2, ['Missing argument']),
    (['scaffold', 'plugin', 'subcommand'], 2, ['Missing argument']),
])
def test_subcommand_stdout(args: list[str], exit_code: int, content: list[str]):
    app = create_cli()
    result = runner.invoke(app, args)
    assert result.exit_code == exit_code
    for c in content:
        assert c in result.stdout
