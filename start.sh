#! /bin/bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
$HOME/.poetry/bin/poetry install
$HOME/.poetry/bin/poetry shell
hypercorn main:app --bind "[::]:8000"