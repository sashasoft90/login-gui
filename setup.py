"""PyPI setup script

Script includes primary Python package along with essential
non-Python files, such as QML, svg and .png resources.

Usage:
    python setup.py sdist
"""

import importlib.machinery
import os
import types

# noinspection PyUnresolvedReferences
from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

version_file = os.path.abspath("commonlib/version.py")
loader = importlib.machinery.SourceFileLoader('version', version_file)
mod = types.ModuleType(loader.name)
loader.exec_module(mod)
version = getattr(mod, 'version')


def get_all_files(qml_dir, list_of_data):
    """
    function parse all file in folder with suffix
    """
    temp_path = qml_dir.replace("\\", "/")
    temp_path = temp_path.replace("commonlib/", "")
    temp_path = temp_path + '/'
    qml_dir = os.path.abspath(qml_dir)
    for root, _, _ in os.walk(qml_dir):
        for suffix in ("ttf", "qml", "js", "txt", "png", "py", "otf", ".svg"):
            rel_path = os.path.relpath(root, qml_dir)
            rel_path = rel_path.replace("\\", "/")
            list_of_data.append(temp_path + rel_path.strip(".") + "/*." + suffix)
    return list_of_data


# Collect non-python data as package data
package_data = list()
package_data = get_all_files('commonlib', package_data)

# get all requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

classifiers = [
    "Development Status :: 2 - Pre-Alpha",  # todo "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]

setup(
    name="commonLib",
    version=version,
    description="",
    long_description=readme,
    author="ESPRiT Engineering GmbH on the commission of BMW Group",
    author_email="alexander.sacharov@esprit-engineering.com",
    url="",  # todo: add repo url
    license="LGPL v3",
    packages=find_packages(),
    zip_safe=False,
    package_data={
        "autool32": package_data
    },
    classifiers=classifiers,
    install_requires=requirements,
)
