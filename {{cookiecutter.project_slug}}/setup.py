from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

version = {}
with open("{{ cookiecutter.project_slug }}/version.py") as f:
    exec(f.read(), version)

setup(
    name="{{ cookiecutter.project_slug }}",
    version=version["__version__"],
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.full_name }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}", "{{ cookiecutter.project_slug }}.*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[],{%- if cookiecutter.command_line_interface|lower == 'y' %}
    entry_points={"console_scripts": ["{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main"]},{%- endif %}
)
