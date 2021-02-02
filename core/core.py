# -*- coding: utf-8 -*-

""" core.core: provides entry point main()."""
from io import BufferedReader

import click
from undictify import type_checked_call

from .config.config import load_core_config
from .config.models import CoreConfig
from .discovery.discover import discover_dependencies
from .discovery.models import DiscoveryReport
from .initialization import init_application

__version__ = "0.1.0"


@click.group()
def main():
    pass


@main.command()
@click.option("--config", "-c", type=click.File("rb"), help="Provide an alternative path to the config.")
@type_checked_call()
def start(config: BufferedReader):

    click.secho(f"Starting BeyondSpaces version {__version__}.", fg="red")
    core_config: CoreConfig = load_core_config()
    report: DiscoveryReport = discover_dependencies(core_config)
    init_application(report)
