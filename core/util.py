import os
import subprocess
from typing import NewType
import click

CliCommand = NewType('CliCommand', list)
DirPath = NewType('DirPath', str)


def run_cli_command(command: CliCommand) -> bytes:
    return subprocess.check_output(command)


def create_directory(dir_path: DirPath):
    try:
        os.mkdir(dir_path)
    except OSError:
        click.echo(f"Creation of the directory {dir_path} failed")
