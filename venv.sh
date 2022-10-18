#!/bin/bash

if [ ! -d ./venv ]; then
  python3 -m venv venv
fi

script_dir=`dirname $0`

cd $script_dir

/bin/bash -c ". ./venv/bin/activate; exec /bin/bash -i"
