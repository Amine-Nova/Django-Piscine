#!/bin/sh

python3 -m pip --version

if [ -d local_lib/path ]; then
    echo "File Already Exists!"
else
    rm -rf local_lib
    git clone --progress https://github.com/jaraco/path.git local_lib 2>&1
fi