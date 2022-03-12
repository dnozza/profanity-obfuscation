=====================
profanity_obfuscation
=====================

Python package for obfuscate profanities.


Installing
----------

.. code-block:: bash

    python3 setup.py install

How To Use
----------

You can obfuscate text as strings:

.. code-block:: python

    import profanity_obfuscation as prof

    obfuscator = prof.Prof()

    obfuscator.obfuscate_string("puta mierda")
    >> 'p*ta m*erda'

Or passing text files (such as .tex):

.. code-block:: python

    with open("paper.tex, 'r') as file:
        text = file.read()

    obfuscated_text = obfuscator.obfuscate_string(text)

    with open("paper_obfuscated.tex", 'w') as f:
        f.write(obfuscated_text)

Software Details
----------

* Free software: MIT license
* Documentation: https://profanity-obfuscation.readthedocs.io.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
