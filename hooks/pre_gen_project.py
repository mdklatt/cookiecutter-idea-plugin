""" Pre-generation tasks.

This is executed before the project has been generated.

"""
def main() -> int:
    """ Validate parameters.

    """
    status = 0
    if not "{{ cookiecutter.plugin_name }}":
        print("ERROR: plugin_name cannot be blank")
        status = 1
    if not "{{ cookiecutter.author_name }}":
        print("ERROR: author_name cannot be blank")
        status = 1    
    return status


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
