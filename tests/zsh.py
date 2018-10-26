#!/usr/bin/env python3
""" Test if we can get a zsh shell with container and shell defined """
import sys

from pathlib import Path

from pexpect import spawn


def main():
    """ Main """
    executable = Path(__file__).absolute().parent.parent / "docker-shell"
    child = spawn(str(executable), args=["shell_zsh_on_jessie", "zsh"])
    child.expect("Trying to execute zsh on shell_zsh_on_jessie ...")
    child.expect("(.+)#")

    child.sendline("env")
    child.expect("DOCKER_SHELL=zsh_on_jessie")

    child.sendline("echo $ZSH_VERSION")
    child.expect("5.6.2")

    child.sendline("exit")
    exit_code = child.wait()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
