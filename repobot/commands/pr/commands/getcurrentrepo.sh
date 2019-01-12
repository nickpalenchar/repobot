#!/usr/bin/env bash

git remote -v | sed -n 's/.*\/\(.*\)\.git.*/\1/p' | head -n 1
