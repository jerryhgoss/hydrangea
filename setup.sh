#! /bin/bash

pip install virtualenv
python3 -m venv venv
source $1


pip install -r requirements.txt

"$@"