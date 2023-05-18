.. _cosmology-install:

************
Installation
************


From Source: Cloning, Building, Installing
==========================================

The latest development version of :mod:`cosmology` can be cloned from `GitHub
<https://github.com/cosmology-api/cosmology>`_ using ``git``

.. code-block:: bash

    git clone https://github.com/cosmology-api/cosmology.git

To build and install the project (from the root of the source tree, e.g., inside
the cloned :mod:`cosmology` directory)

.. code-block:: bash

    python -m pip install [-e] .


Python Dependencies
===================

This package has the following dependencies:

* `Python`_ >= 3.9

Explicit version requirements are specified in the project `pyproject.toml
<https://github.com/cosmology-api/cosmology/blob/main/pyproject.toml>`_.
``pip`` and ``conda`` should install and enforce these versions automatically.
