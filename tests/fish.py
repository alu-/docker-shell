#!/usr/bin/env python3
""" Test if we can get a fish shell with container and shell defined """
import sys

from pathlib import Path

from pexpect import spawn


def main():
    """ Main """
    executable = Path(__file__).absolute().parent.parent / "docker-shell"
    child = spawn(str(executable), args=["shell_fish_on_alpine", "fish"])
    child.expect("Trying to execute fish on shell_fish_on_alpine ...")
    child.expect("Welcome to fish, the friendly interactive shell")
    child.expect("Type (.+) for instructions on how to use fish")
    child.expect("(.*)root@(.+) (.*)#(.*)")

    child.sendline("env")
    child.expect("DOCKER_SHELL=fish_on_alpine")

    child.sendline("echo $SHELL")
    child.expect("/usr/bin/fish")

    child.sendline("exit")
    exit_code = child.wait()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
