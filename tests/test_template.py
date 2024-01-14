""" Test the Cookiecutter template.

A template project is created in a temporary directory, the plugin is built in
a self-contained environment, and the plugin test suite is run.

"""
import pytest
from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from pathlib import Path
from shlex import split
from subprocess import run


@pytest.fixture(scope="module")
def template() -> Path:
    """ The template under test.

    """
    return Path(__file__).resolve().parents[1]


@pytest.fixture()
def tmpdir(tmp_path_factory) -> Path:
    """ Session test directory.

    """
    return tmp_path_factory.mktemp("test_template")


@pytest.fixture()
def context(template) -> dict:
    """ Template context for testing.

    """
    context = generate_context(template.joinpath("cookiecutter.json"))
    context["cookiecutter"].update({
        "author_name": "J. Doe",
        "compact_dirs": "no",
        "junit_runner": "yes",
    })
    return context["cookiecutter"]


@pytest.fixture()
def project(tmpdir, template, context) -> Path:
    """ Create a test project from the Cookiecutter template.

    """
    cookiecutter(str(template), no_input=True, output_dir=tmpdir, extra_context=context)
    return tmpdir / context["plugin_name"]


def test_project(project):
    """ Verify that the project was created correctly.

    """
    assert len(list(project.iterdir())) == 12
    return


def test_build(tmpdir, project):
    """ Verify that the project builds correctly.

    """
    home = tmpdir / "home" / ".gradle"
    gradle = f"./gradlew --gradle-user-home={home} check"
    process = run(split(gradle), cwd=project)
    assert process.returncode == 0
    return
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
