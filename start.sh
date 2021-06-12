#! /bin/bash
pip3 install poetry
poetry install
hypercorn main:app --bind "[::]:8000"