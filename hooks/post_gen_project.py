""" Post-generation tasks.

This is executed after the project has been generated.

"""
from pathlib import Path


def main() -> int:
    """ Execute all tasks.

    """
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


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
