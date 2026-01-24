#!/bin/bash

CONTAINER_CMD=$(which podman || which docker)

$CONTAINER_CMD build -t localhost/website-django-cms:staging -f Dockerfile

