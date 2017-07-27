#!/bin/bash
echo 'Stopping and removing old container'
docker kill Infectiious_APICollect
docker container rm Infectiious_APICollect
echo 'Rebuilding image...'
docker build -t infectiious_python .
echo 'Starting container.'
docker run -d --name Infectiious_APICollect infectiious_python
