"""
major, minor, patch version of autool32
"""
VERSION_MAJOR = 2
VERSION_MINOR = 0
VERSION_PATCH = 0

version_info = (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
version = '%i.%i.%i' % version_info
__version__ = version

__all__ = ['version', 'version_info', '__version__']
