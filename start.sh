#! /bin/bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
poetry install
hypercorn main:app --bind "[::]:8000"