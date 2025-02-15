#! /bin/bash

docker build \
    --force-rm \
    --no-cache \
    -t what-ya-wanna-read \
    -f Dockerfile .
