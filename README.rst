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

The ``compact_dirs`` template parameter controls whether or not to use a
compact `Kotlin directory structure`_ or a traditional Java structure that
starts at the package root.


=====
Usage
=====

Install Python requirements for using the template:

.. code-block:: console

  $ python -m pip install cookiecutter==2.1.0


Create a new project directly from the template on `GitHub`_:

.. code-block:: console

  $ cookiecutter gh:mdklatt/cookiecutter-idea-plugin


.. |badge| image:: https://github.com/mdklatt/cookiecutter-idea-plugin/actions/workflows/test.yml/badge.svg
    :alt: GitHub Actions status
    :target: `GitHub Actions`_
.. _GitHub Actions: https://github.com/mdklatt/cookiecutter-idea-plugin/actions/workflows/test.yml
.. _Cookiecutter: https://cookiecutter.readthedocs.org
.. _JetBrains IDEA plugin: https://github.com/JetBrains/intellij-platform-plugin-template
.. _IntelliJ Platform Plugin Template: https://plugins.jetbrains.com/docs/intellij/welcome.html
.. _Kotlin: https://kotlinlang.org
.. _Gradle: https://gradle.org
.. _JUnit: https://junit.org
.. _GitHub: https://github.com/mdklatt/cookiecutter-idea-plugin
.. _Gradle Wrapper: https://docs.gradle.org/current/userguide/gradle_wrapper.html
.. _Kotlin directory structure: https://kotlinlang.org/docs/coding-conventions.html#directory-structure
