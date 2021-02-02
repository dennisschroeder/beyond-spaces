from dataclasses import dataclass

from undictify import type_checked_constructor


@type_checked_constructor()
@dataclass
class PlatformInformation:
    platform: str
    python_version: str


@type_checked_constructor()
@dataclass
class DiscoveryReport:
    platform_information: PlatformInformation
    user_config_available: bool
    not_installed_executables: list
    not_installed_apps: list
