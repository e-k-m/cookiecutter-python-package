from contextlib import contextmanager
from pathlib import Path
import os
import shlex
import shutil
import subprocess


from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from cookiecutter.prompt import prompt_for_config


def project_info(result):
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


@contextmanager
def inside_dir(dirpath):
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def run_inside_dir(command, dirpath):
    with inside_dir(dirpath):
        return subprocess.check_call(
            shlex.split(command),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        shutil.rmtree(result.project)


class Result(object):
    def __init__(
        self, exception=None, exit_code=0, project_dir=None, context=None
    ):
        self.exception = exception
        self.exit_code = exit_code
        self.context = context
        self._project_dir = project_dir

    @property
    def project(self):
        if self.exception is None:
            return Path(self._project_dir)
        return None

    def __repr__(self):
        if self.exception:
            return "<Result {!r}>".format(self.exception)

        return "<Result {}>".format(self.project)


class Cookies(object):
    def __init__(self, template, output_factory, config_file):
        self._default_template = template
        self._output_factory = output_factory
        self._config_file = config_file
        self._counter = 0

    def _new_output_dir(self):
        dirname = "bake{:02d}".format(self._counter)
        output_dir = self._output_factory(dirname)
        self._counter += 1
        return output_dir

    def bake(self, extra_context=None, template=None):
        exception = None
        exit_code = 0
        project_dir = None
        context = None

        if template is None:
            template = self._default_template

        context_file = (Path(template) / ("cookiecutter.json")).resolve()

        try:
            context = prompt_for_config(
                generate_context(
                    context_file=str(context_file), extra_context=extra_context
                ),
                no_input=True,
            )

            project_dir = cookiecutter(
                template,
                no_input=True,
                extra_context=extra_context,
                output_dir=str(self._new_output_dir()),
                config_file=str(self._config_file),
            )
        except SystemExit as e:
            if e.code != 0:
                exception = e
            exit_code = e.code
        except Exception as e:
            exception = e
            exit_code = -1

        return Result(
            exception=exception,
            exit_code=exit_code,
            project_dir=project_dir,
            context=context,
        )
