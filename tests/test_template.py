""" Test the Cookiecutter template.

A template project is created in a temporary directory, the plugin is built in
a self-contained environment, and the plugin test suite is run.

"""
from json import loads
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter


def main() -> int:
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    defaults = loads(template.joinpath("cookiecutter.json").read_text())
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        home = tmpdir / "home"
        cookiecutter(str(template), no_input=True, output_dir=tmpdir)
        cwd = tmpdir / defaults["project_slug"]
        gradle = f"./gradlew --gradle-user-home={home}/.gradle check"
        check_call(split(gradle), cwd=cwd)
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
