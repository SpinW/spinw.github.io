Installation
============

Prerequisite
-------------

* An installation of Python, version 3.10 or above. Python 3.12 is recommended.
* Recommended: an Integrated Development Environment (IDE), such as VSCode or
  PyCharm.

How to install pySpinW
----------------------

We recommend that you use a virtual environment. See below for details.
pySpinW is available through pip, so to install you simply type:

.. code-block:: console

   pip install pyspinw

Updating
--------

Updating to the latest pySpinW can be done through pip:

.. code-block:: console

   pip install --upgrade pyspinw

Setting up a virtual environment
--------------------------------

Windows
~~~~~~~

Many IDEs automatically set this up for you, so using your IDE's tools is the
recommended method. However, here is how to do it from the terminal.

If you have a modern Python setup, you can create a Python 3.12 virtual
environment with:

.. code-block:: console

   py -3.12 -m venv VENV_NAME

where ``VENV_NAME`` is an arbitrary name for your virtual environment. Many
people use ``.venv``.

If you do not have a modern setup that supports the ``py`` command, you can
use the following, as long as your Python version is newer than 3.10:

.. code-block:: console

   python -m venv VENV_NAME

Then activate this environment with:

.. code-block:: console

   VENV_NAME\Scripts\Activate

Depending on how you are running this, you might need to run this first:

.. code-block:: console

   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

MacOS and Linux
~~~~~~~~~~~~~~~

You can create a Python virtual environment with:

.. code-block:: console

   python -m venv VENV_NAME

where ``VENV_NAME`` is an arbitrary name for your virtual environment. Many
people use ``.venv``.

To activate it, use:

.. code-block:: console

   source VENV_NAME/bin/activate

Conda
~~~~~

Alternatively, you can install a virtual environment using the ``conda`` or
``mamba`` program. First download and install it, then create a virtual
environment called ``pyspinw``:

.. code-block:: console

   mamba create -n pyspinw python=3.12

Then activate this environment and install pySpinW as above:

.. code-block:: console

   mamba activate pyspinw
   pip install pyspinw

Jupyter
~~~~~~~

Many of the tutorials use Jupyter notebooks, which can be installed using:

.. code-block:: console

   pip install notebook

Have fun!
---------
