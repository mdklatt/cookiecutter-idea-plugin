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
    _expand_dirs()
    return 0


def _expand_dirs():
    """ Create source subdirectories for the package hierarchy.

    If the `compact_dirs` template parameter is `yes`, a Kotlin-style compact
    hierarchy is used. Otherwise, a traditional Java hierarchy rooted at the
    package root is created.

    <https://kotlinlang.org/docs/coding-conventions.html#directory-structure>
    """
    # TODO: Use a bool for `compact_dirs` once Cookiecutter adds support.
    compact = "{{ cookiecutter.compact_dirs }}".lower()
    package = "{{ cookiecutter.plugin_package }}"
    if not package or compact == "yes":
        # Use existing structure rooted at the top-level source directories.
        return
    for root in (Path(item, "kotlin") for item in Path("src").iterdir()):
        # Create a subdirectory for every package component,
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
