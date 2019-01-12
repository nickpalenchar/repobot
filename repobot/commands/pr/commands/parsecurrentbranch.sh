#!/bin/bash

echo $(git branch | grep \*|cut -c3-))
