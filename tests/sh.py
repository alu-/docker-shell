#!/usr/bin/env python3
from sys import exit
from pathlib import Path

from pexpect import spawn


def main():
    executable = Path(__file__).absolute().parent.parent / "docker-shell"
    child = spawn(str(executable), args=["sh_on_alpine", "sh"])
    child.expect("Trying to execute sh on sh_on_alpine ...")
    child.expect("/ #")

    child.sendline("env")
    child.expect("DOCKER_SHELL=sh_on_alpine")

    child.sendline("exit")
    exit_code = child.wait()
    exit(exit_code)


if __name__ == '__main__':
    main()
