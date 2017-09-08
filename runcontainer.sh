#!/bin/bash
echo 'Stopping and removing old container'
docker kill PharaohScript_Container >/dev/null
docker container rm PharaohScript_Container >/dev/null

echo 'Rebuilding image...'
docker build -t PharaohScript_image . >>./buildcontainer.log

echo 'Starting container.'
docker run -d --name PharaohScript_Container PharaohScript_image >/dev/null
echo 'Container running as PharaohScript_Container'
