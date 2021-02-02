# -*- coding: utf-8 -*-

""" core.config.models: provides config model objects."""

from dataclasses import dataclass
from typing import List
from undictify import type_checked_constructor


@type_checked_constructor()
@dataclass
class Discovery:
    installed: List[str]
    executable: List[str]


@type_checked_constructor()
@dataclass
class UserStorage:
    location: str
    files: List[str]


@type_checked_constructor()
@dataclass
class UserConfig:
    location: str
    filename: str


@type_checked_constructor()
@dataclass
class CoreConfig:
    discovery: Discovery
    user_config: UserConfig
    user_storage: UserStorage
