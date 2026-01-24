#!/bin/bash

CONTAINER_CMD=$(which podman || which docker)

$CONTAINER_CMD tag localhost/website-django-cms:staging registry.bristolhackspace.org/website-django-cms:staging

$CONTAINER_CMD push registry.bristolhackspace.org/website-django-cms:staging

