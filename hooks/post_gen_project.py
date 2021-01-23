import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(os.path.join(PROJECT_DIRECTORY, path))


if __name__ == "__main__":
    if "y" not in "{{ cookiecutter.command_line_interface|lower }}":
        remove(os.path.join("{{ cookiecutter.project_slug }}", "cli.py"))

    if "y" not in "{{ cookiecutter.github_actions|lower }}":
        remove(".github")
