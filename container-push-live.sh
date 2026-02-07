#!/bin/bash

CONTAINER_CMD=$(which podman || which docker)

$CONTAINER_CMD tag registry.bristolhackspace.org/website-django-cms:staging registry.bristolhackspace.org/website-django-cms:live

$CONTAINER_CMD push registry.bristolhackspace.org/website-django-cms:live

