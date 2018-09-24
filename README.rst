Setup
=====

Virtualenv + deps::

    python3 -m venv venv
    venv/bin/pip install --upgrade pip setuptools
    venv/bin/pip install docutils black

Clone destination::

    git clone git@github.com:pound-python/pound-python.github.io.git

Build::

    venv/bin/python3 build.py

Output HTML will be in the pound-python.github.io/ repo. Commit and push
in that repo to publish.


Use `Black <https://github.com/ambv/black>`_ to format the build script.
