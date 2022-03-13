# Profanity Obfuscation

Python package for obfuscating profanities.


## Installing

    python3 setup.py install

## How To Use

You can obfuscate text as strings, eventually specifying the language:


    import profanity_obfuscation as prof

    obfuscator = prof.Prof()

    obfuscator.obfuscate_string("puta mierda")
    >> 'p*ta m*erda'

    obfuscator.obfuscate_string("porca puttana","IT")
    >> 'p*rca p*ttana'

Or passing text files (such as .tex):

    with open("paper.tex, 'r') as file:
        text = file.read()

    obfuscated_text = obfuscator.obfuscate_string(text)

    with open("paper_obfuscated.tex", 'w') as f:
        f.write(obfuscated_text)

You can also use the library to reveal profanities from their obfuscated versions:

    obfuscator.reveal_profanity("m*erda")
    >> 'mierda'

## Software Details

* Free software: MIT license
* Documentation: https://profanity-obfuscation.readthedocs.io.


## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
