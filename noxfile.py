import nox

REQUIRES = {
    "bake": ["cookiecutter>=1.6.0,<2.0.0"],
    "test": ["cookiecutter>=1.6.0,<2.0.0", "nox"],
    "fmt": ["black>=19.10b0,<20.00"],
    "lint": ["flake8>=3.7.9,<4.0.0"],
}


def install(session, *names):
    for e in names:
        session.install(*REQUIRES[e])


@nox.session
def devel(session):
    install(session, "bake", "test", "fmt", "lint")


@nox.session
def bake(session):
    install(session, "bake")
    session.run("cookiecutter", "--no-input", "--overwrite-if-exists", ".")


@nox.session
def test(session):
    install(session, "test")
    session.run("python", "-m", "unittest", "discover", "tests")


@nox.session
def fmt(session):
    install(session, "fmt")
    session.run("black", "-l", "79", "hooks", "tests", "noxfile.py")


@nox.session
def lint(session):
    install(session, "lint")
    session.run("flake8", "hooks", "tests", "noxfile.py")
