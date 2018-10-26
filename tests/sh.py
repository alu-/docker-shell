#!/usr/bin/env python3
""" Test if we can get a sh shell with container and shell defined """
import sys

from pathlib import Path

from pexpect import spawn


def main():
    """ Main """
    executable = Path(__file__).absolute().parent.parent / "docker-shell"
    child = spawn(str(executable), args=["shell_sh_on_alpine", "sh"])
    child.expect("Trying to execute sh on shell_sh_on_alpine ...")
    child.expect("/ #")

    child.sendline("env")
    child.expect("DOCKER_SHELL=sh_on_alpine")

    child.sendline("cat /proc/$$/cmdline")
    child.expect("sh")

    child.sendline("exit")
    exit_code = child.wait()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
