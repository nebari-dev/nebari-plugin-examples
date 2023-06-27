from nebari.hookspecs import hookimpl

import typer


@hookimpl
def nebari_subcommand(cli):
    @cli.command()
    def hello(
        name: str = typer.Option(
            "Nebari", help="Who to say hello to"
        )
    ):
        print(f"Hello {name}")
