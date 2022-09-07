""" Post-generation tasks.

This is executed after the project has been generated.

"""
from pathlib import Path
from shlex import split
from subprocess import run


def main() -> int:
    """ Execute all tasks.

    """
    _gradlew()
    _src_dir()
    return 0


def _src_dir():
    """ Place source files into the package hierarchy.

    """
    package = "{{ cookiecutter.package_name }}"
    if not package:
        return
    for module in Path("src").iterdir():
        root = Path(module, "kotlin")
        items = list(root.iterdir())
        leaf = root.joinpath(*package.split("."))
        leaf.mkdir(parents=True)
        for item in items:
            # Move items into package directory.
            item.rename(leaf / item.name)
    return


def _gradlew():
    """ Update Gradle Wrapper to the requested version.

    """
    command = "./gradlew wrapper --gradle-version {{ cookiecutter.gradle_version }}"
    run(split(command), check=True)
    return


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
