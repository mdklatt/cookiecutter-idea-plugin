############################
IDEA Plugin Project Template
############################

|badge|

This is a `Cookiecutter`_ template for creating a `JetBrains IDEA plugin`_
project using `Kotlin`_. The template is adapted from the
`IntelliJ Platform Plugin Template`_.

================
Project Features
================

- `Kotlin`_
- `Gradle`_ builds using a self-contained `Gradle Wrapper`_.
- `JUnit`_ test suite
- IDEA platform 2022.1+ (Java 11)


=====
Usage
=====

Install Python requirements for using the template:

.. code-block:: console

  $ python -m pip install --requirement=requirements-dev.txt


Create a new project directly from the template on `GitHub`_:

.. code-block:: console

  $ cookiecutter gh:mdklatt/cookiecutter-idea-plugin


.. |badge| image:: https://github.com/mdklatt/idea-remotepython-plugin/actions/workflows/build.yml/badge.svg
    :alt: Travis CI build status
.. _Cookiecutter: https://cookiecutter.readthedocs.org
.. _JetBrains IDEA plugin: https://github.com/JetBrains/intellij-platform-plugin-template
.. _IntelliJ Platform Plugin Template: https://plugins.jetbrains.com/docs/intellij/welcome.html
.. _Kotlin: https://kotlinlang.org
.. _Gradle: https://gradle.org
.. _JUnit: https://junit.org
.. _GitHub: https://github.com/mdklatt/cookiecutter-idea-plugin
.. _Gradle Wrapper: https://docs.gradle.org/current/userguide/gradle_wrapper.html
