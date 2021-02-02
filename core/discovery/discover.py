# -*- coding: utf-8 -*-

""" core.discovery.discover: provides system based discoveries."""

import os
import platform
from typing import NewType

from distutils.spawn import find_executable

from undictify import type_checked_call

from .models import DiscoveryReport, PlatformInformation
from ..config.models import CoreConfig

MacOSApp = NewType("MacOSApp", str)

UserConfigPath = NewType('UserConfigPath', str)


def get_users_home_directory():
    return os.path.expanduser("~")


@type_checked_call()
def discover_dependencies(core_config: CoreConfig) -> DiscoveryReport:
    executable_apps_to_discover = core_config.discovery.executable
    installed_apps_to_discover = core_config.discovery.installed

    missing_executables = \
        [name for name in executable_apps_to_discover if not is_app_executable(MacOSApp(name))]

    missing_installed_apps = \
        [name for name in installed_apps_to_discover if not is_application_installed(MacOSApp(name))]

    return DiscoveryReport(
        platform_information=retrieve_platform_information(),
        not_installed_executables=missing_executables,
        not_installed_apps=missing_installed_apps,
        user_config_available=False
    )


def is_user_config_available(config: UserConfigPath) -> bool:
    return os.path.isfile(config)


def is_application_installed(name: MacOSApp) -> bool:
    for app in os.listdir('/Applications'):
        if app == "{name}.app".format(name=name):
            return True
    return False


def is_app_executable(name: MacOSApp) -> bool:
    return find_executable(name) is not None


def retrieve_platform_information() -> PlatformInformation:
    return PlatformInformation(platform=platform.platform(), python_version=platform.python_version())
