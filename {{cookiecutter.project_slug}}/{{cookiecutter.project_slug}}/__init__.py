"""
{{ cookiecutter.project_short_description }}

Example
-------
To use {{ cookiecutter.project_slug }} from code, do:

import {{ cookiecutter.project_slug }}
{{ cookiecutter.project_slug }}.say('I love batman')

Or you can also the CLI and do:
{{ cookiecutter.project_slug }} I love batman
"""

from {{ cookiecutter.project_slug }} import version
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import say

__author__ = "{{ cookiecutter.full_name }}"
__version__ = version.__version__
__all__ = [say]
