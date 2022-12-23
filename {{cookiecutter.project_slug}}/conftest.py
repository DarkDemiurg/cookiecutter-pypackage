"""Pytest setup"""


def pytest_configure(config):
    # NB this causes `{{cookiecutter.pkg_name}}/__init__.py` to run
    import {{cookiecutter.pkg_name}}  # noqa
