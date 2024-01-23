import click

from w95kg import __version__
from w95kg.keys import OEMKey, OfficeKey, RetailKey


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__)
def cli() -> None:
    """Windows 95 and Office 97 key generator and validator.

    Copyright (c) 2024 frosty.
    """
    pass


@cli.command(name="validate")
@click.argument("key", type=str)
def validate_command(key: str) -> None:
    """Validate a key."""

    if OEMKey.validate(key):
        click.echo("OEM key is valid")
    elif RetailKey.validate(key):
        click.echo("Retail key is valid")
    elif OfficeKey.validate(key):
        click.echo("Office 97 key is valid")
    else:
        click.echo("Key is invalid")


@cli.command(name="generate")
@click.argument(
    "type",
    type=click.Choice(["oem", "retail", "office", "all"]),
    default="all",
)
def generate_command(type: str) -> None:
    """Generate a key."""

    match type:
        case "oem":
            click.echo(f"OEM key: {OEMKey.generate()}")
        case "retail":
            click.echo(f"Retail key: {RetailKey.generate()}")
        case "office":
            click.echo(f"Office 97 key: {OfficeKey.generate()}")
        case "all":
            click.echo(f"OEM key: {OEMKey.generate()}")
            click.echo(f"Retail key: {RetailKey.generate()}")
            click.echo(f"Office 97 key: {OfficeKey.generate()}")


if __name__ == "__main__":
    cli()
