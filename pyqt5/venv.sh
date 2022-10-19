#!/bin/bash

if [ ! -d ./venv ]; then
  brew cat pyqt@5 | grep 'depends_on.*python'
  /opt/homebrew/bin/python3.9 -m venv --system-site-packages venv
fi

script_dir=`dirname $0`

cd $script_dir

/bin/bash -c ". ./venv/bin/activate; exec /bin/bash -i"
