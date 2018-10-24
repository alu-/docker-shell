# docker-shell
Gives you a shell in a running Docker container.

### Usage

```shell
Usage:
  docker-shell [CONTAINER] [SHELL]
  docker-shell --help|-h|-?
  docker-shell --version|-v

Arguments:
  CONTAINER       Name of the container
  SHELL           Force a specific shell, otherwise pick 'best' shell
                  [bash fish zsh tcsh csh ksh sh]
  -h, -?, --help  Print this help text
  -v, --version   Print version and exit

Note:
  If the container name is omitted then the newest container will be used.
  Container name will match any part of name with wildcards.
  E.g 'web' and 'ebserv' will both match 'webserver'.
  If container name matches more than one container the latest one will be used.

Author:
  Oskar Andersson <alu@byteberry.net>
```
