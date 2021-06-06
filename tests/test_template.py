""" Test the Cookiecutter template.

A template project is created in a temporary directory, the plugin is built in
a self-contained environment, and the plugin test suite is run.

"""
from json import loads
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.config import get_user_config
from cookiecutter.main import cookiecutter


def main() -> int:
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    context = loads(template.joinpath("cookiecutter.json").read_text())
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        kwargs = {
            "extra_context": {"plugin_name": "Test", "author_name": "Author"},
            "no_input": True,
            "output_dir": tmpdir,
        }
        cookiecutter(str(template), **kwargs)
        cwd = tmpdir / context["project_slug"]
        home = tmpdir / "home"
        for task in "check", "runPluginVerifier":
            gradle = f"./gradlew --gradle-user-home={home}/.gradle {task}"
        check_call(split(gradle), cwd=cwd)
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
