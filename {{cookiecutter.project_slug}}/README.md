# {{ cookiecutter.project_slug }}

{%- if cookiecutter.github_actions|lower == 'y' %}

![](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/main/badge.svg)
{%- endif %}

```text
                    I love batman
                     /
    =/\             /   /\=
    / \'._   (\_/) / _.'/ \
   / .''._'--(o.o)--'_.''. \
  /.' _/ |`'=/ " \='`| \_ `.\
 /` .' `\;-,'\___/',-;/` '. '\
/.-'       `\(-V-)/`       `-.\
`            "   "
```

> like cowsay but with a bat

[Installation](#installation) | [Getting Up And Running](#getting-up-and-running) | [Examples](#examples) | [API](#api) | [See Also](#see-also)

{{ cookiecutter.project_slug }} is like cowsay but with a bat. The main feature are:

- Can be used as a package,

- or directly from the CLI

- to print messages of a bat saying things.

## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

## Getting Up and Running

```bash
nox -l
```

## Examples

```python
import {{ cookiecutter.project_slug }}

r = {{ cookiecutter.project_slug }}.say('I love batman')
print(r) # will print the bat saying 'I love batman'


# or using the CLI {{ cookiecutter.project_slug }} I love batman
```

## API

```text 
FIXME
```

## See Also

- [CHANGELOG](./CHANGELOG.md)
