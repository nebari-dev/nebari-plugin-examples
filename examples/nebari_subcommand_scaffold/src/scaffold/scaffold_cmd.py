# https://github.com/nebari-dev/nebari/pull/1833

import typer

from .subcommands.plugin import plugin_cmd as plugin

from nebari.hookspecs import hookimpl

@hookimpl
def nebari_subcommand(cli: typer.Typer):
    app = typer.Typer()
    cli.add_typer(app, name = 'scaffold', help = 'Generate standard file/folder content for various Nebari components.', rich_help_panel = 'Additional Commands')

    app.add_typer(plugin.app, name = 'plugin', help = 'Generate standard project structure for a Nebari plugin.')
