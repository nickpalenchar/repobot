# Repobot - CLI for github actions

## Install

Requires python3.6 or higher.

```shell
$ pip3 install repobot
```

## Setting up

After installing, simply set your login credentials.

```shell
$ rbot login
Github username: username
Password: ****

Successfully Authenticated.
```

> NOTE: You can call the cli with `repobot` as well, but `rbot` is more convienent :)

## Examples

### Create a new repository interactively

```
$ rbot new
# follow the prompts!
```

### Create a new repository with all default values

```
$ rbot new -D reponame
```

### Create a new private repository in an organization you belong to

```
$ rbot new --private --org=myorg reponame
```

### list your repositories (first 30)

```
$ rbot ls
```

### list all your repositories

```
$ rbot ls --all
```

### Learn more about the CLI

```
$ rbot --help
```

### Learn more about a particular command

```
$ rbot new --help
$ rbot pr new --help
```
