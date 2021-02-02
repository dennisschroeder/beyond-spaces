# -*- coding: utf-8 -*-

""" core.initialization.init: runs the initialization process."""

import click
from undictify import type_checked_call
from .discovery.models import DiscoveryReport


@type_checked_call()
def init_application(report: DiscoveryReport):
    """ Initializes the application."""

    click.secho("Starting to initialize BeyondSpaces...")

    if not report.platform_information.platform.startswith("mac_OS"):
        click.secho("BeyondSpaces does not run on your system!", bg="red", fg="white")
        result: str = click.prompt("Do you want some more information on how to run BeyondSpaces? [Yes/No]")
        if result == "Yes" or result == "yes":
            click.echo("Do yourself a favor and get a Mac...")
            click.launch("https://www.apple.com/de/mac/")

    if not report.user_config_available:
        click.secho("")
