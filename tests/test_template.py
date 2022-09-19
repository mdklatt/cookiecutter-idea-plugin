""" Test the Cookiecutter template.

A template project is created in a temporary directory, the plugin is built in
a self-contained environment, and the plugin test suite is run.

"""
from cookiecutter.generate import generate_context
from cookiecutter.main import cookiecutter
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory


def main() -> int:
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    context = generate_context()["cookiecutter"]
    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        kwargs = {
            "extra_context": {
                "author_name": "Author",
                "junit_runner": "JUnit",
                "compact_dirs": "no",  # test directory expansion
            },
            "no_input": True,
            "output_dir": tmpdir,
        }
        cookiecutter(str(template), **kwargs)
        cwd = tmpdir / context["plugin_name"]
        home = tmpdir / "home"
        for task in "check", "runPluginVerifier":
            gradle = f"./gradlew --gradle-user-home={home}/.gradle {task}"
        check_call(split(gradle), cwd=cwd)
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
