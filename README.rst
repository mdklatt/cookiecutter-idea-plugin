############################
IDEA Plugin Project Template
############################

|badge|

This is a `Cookiecutter`_ template for creating a `JetBrains IDEA plugin`_ 
project. The template is adapted from the `IntelliJ Platform Plugin Template`_.


================
Project Features
================

- `Kotlin`_
- `Gradle`_ builds
- `JUnit`_ test suite


=====
Usage
=====

Install Python requirements for using the template:

.. code-block:: console

  $ python -m pip install --user --requirement=requirements.txt


Create a new project directly from the template on `GitHub`_:

.. code-block:: console

  $ cookiecutter gh:mdklatt/cookiecutter-idea-plugin


.. _travis: https://travis-ci.com/mdklatt/cookiecutter-idea-plugin
.. |badge| image:: https://travis-ci.com/mdklatt/cookiecutter-idea-plugin.png
    :alt: Travis CI build status
    :target: `travis`_
.. _Cookiecutter: https://cookiecutter.readthedocs.org
.. _JetBrains IDEA plugin: https://github.com/JetBrains/intellij-platform-plugin-template
.. _IntelliJ Platform Plugin Template: https://plugins.jetbrains.com/docs/intellij/welcome.html
.. _Kotlin: https://kotlinlang.org
.. _Gradle: https://gradle.org
.. _JUnit: https://junit.org
.. _GitHub: https://github.com/mdklatt/cookiecutter-idea-plugin
