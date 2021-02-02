# -*- coding: utf-8 -*-

""" core.__init__: provides at initialization ready objects."""
import json
import sys
import click
from pkg_resources import resource_filename
from ruamel.yaml import YAML

from core.config.models import CoreConfig, Discovery, UserConfig, UserStorage


def load_core_config() -> CoreConfig:
    yaml_parser = YAML()
    config_file_path = resource_filename("core", "config.yaml")

    with open(config_file_path, "r") as file:
        parsed_yaml = yaml_parser.load(file)

    return CoreConfig(**parsed_yaml)
