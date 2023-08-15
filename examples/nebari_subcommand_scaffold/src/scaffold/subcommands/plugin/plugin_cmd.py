import typer

from .stage import stage_runner as _stage
from .subcommand import subcommand_runner as _subcommand

app = typer.Typer()

@app.command()
def stage(
    ctx: typer.Context,
    name: str = typer.Argument(..., help = 'Name of the stage', show_default = False),
    priority: int = typer.Argument(..., help = 'Priority of the stage', show_default = False),
    # priority: int = typer.Option(..., '--priority', '-p', help = 'Priority of the stage', show_default = False, prompt = True),
    out: str = typer.Option(..., '--out', '-o', help = 'Output directory', show_default = False),
    type: _stage.StagePluginType = typer.Option(_stage.StagePluginType.default, '--type', '-t', help = 'Base type of the stage', case_sensitive = False),
    ):
    """
    Nebari stage type plugin.
    """
    _stage.run(name, priority, out, type)

@app.command()
def subcommand(
    ctx: typer.Context,
    name: str = typer.Argument(..., help = 'Name of the generated plugin.', show_default = False),
    out: str = typer.Option(..., '--out', '-o', help = 'Output directory.', show_default = False),
    force: bool = typer.Option(False, '--force', '-f', help = 'Overwrite output directory if exists.', show_default = True),
    ):
    """
    Nebari subcommand type plugin.
    """
    _subcommand.run(name, out, force)
