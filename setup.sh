#!/bin/bash

if [ ! -d "venv" ]; then
  virtualenv venv
  source venv/Scripts/activate
  pip install -r requirements.txt
fi
