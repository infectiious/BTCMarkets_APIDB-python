#!/bin/bash
echo 'Stopping and removing old container'
docker kill Infectiious_APICollect >/dev/null
docker container rm Infectiious_APICollect >/dev/null

echo 'Rebuilding image...'
docker build -t infectiious_python . >>./buildcontainer.log

echo 'Starting container.'
docker run -d --name Infectiious_APICollect infectiious_python >/dev/null
echo 'Container running as Infectiious_APICollect'
