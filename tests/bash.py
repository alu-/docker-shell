#!/usr/bin/env python3
""" Test if we can get a bash shell with container and shell defined """
import sys

from pathlib import Path

from pexpect import spawn


def main():
    """ Main """
    executable = Path(__file__).absolute().parent.parent / "docker-shell"
    child = spawn(str(executable), args=["shell_bash_on_ubuntu", "bash"])
    child.expect("Trying to execute bash on shell_bash_on_ubuntu ...")
    child.expect("root@(.+):/#")

    child.sendline("env")
    child.expect("DOCKER_SHELL=bash_on_ubuntu")

    child.sendline("echo $SHELL")
    child.expect("/bin/bash")

    child.sendline("exit")
    exit_code = child.wait()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
