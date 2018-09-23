Setup
=====

Virtualenv + deps::

    python3 -m venv venv
    venv/bin/pip install --upgrade pip setuptools
    venv/bin/pip install docutils black

Build::

    venv/bin/python3 build.py

Output HTML will be in the output/ dir.


Use `Black <https://github.com/ambv/black>`_ to format the build script.
