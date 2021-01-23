"""
CLI of {{ cookiecutter.project_slug }}.

Usage
-----
{{ cookiecutter.project_slug }} I love batman

or

python -m {{ cookiecutter.project_slug }}.cli my I love batman
"""

import argparse
import sys

import {{ cookiecutter.project_slug }}


def main():
    parser = argparse.ArgumentParser(description="{{ cookiecutter.project_slug }} <some message>")
    parser.add_argument("message", nargs="*")
    args = " ".join(parser.parse_args().message)
    if args:
        print({{ cookiecutter.project_slug }}.say(args))
    else:
        print({{ cookiecutter.project_slug }}.say("no message"))


if __name__ == "__main__":
    sys.exit(main())
