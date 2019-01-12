#!/usr/bin/env bash

REMOTE=$(git remote show)

if (( $(echo $E | wc -l) > 0)); then
  exit 10
fi

echo $(git remote show $REMOTE | grep HEAD | cut -d ":" -f 2)
