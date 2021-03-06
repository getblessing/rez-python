
early = globals()["early"]


name = "python"

authors = ["Guido van Rossum"]

description = "The Python programming language"


@early()
def version():
    """Define Python version from command line option
    """
    import sys
    import argparse

    if any(help_ in sys.argv[1:] for help_ in ["-h", "--help"]):
        # Skip parsing version string if user is asking for help,
        # or the following parser will print out it's own help
        # message without rez-build's.
        return ""

    parser = argparse.ArgumentParser()

    with open("./parse_build_args.py", "r") as add_args:
        exec(add_args.read(), {"parser": parser})

    args, unknown = parser.parse_known_args()  # parse `sys.argv`
    local_patch = "+1"
    python_version = args.version + local_patch

    return python_version

tools = [
    "python",
    "pythonw",
    "pip",
]

variants = [
    ["platform-*"],
]


private_build_requires = ["rezutil-1"]
build_command = "python {root}/rezbuild.py {install}"


def commands():
    env = globals()["env"]
    system = globals()["system"]

    if system.platform == "windows":
        env.PATH.prepend("{root}/payload")
        env.PATH.prepend("{root}/payload/Scripts")
    else:
        # untested
        env.PATH.prepend("{root}/payload/bin")


uuid = "repository.python"
