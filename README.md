# Profanity Obfuscation

[Debora Nozza](https://deboranozza.com/) · [Dirk Hovy](http://www.dirkhovy.com/)

Python package for obfuscating profanities, appearing in ACL 2023.

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

    with open("paper.tex", 'r') as file:
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


## Reference

If you use this tool please cite the following paper:

       @inproceedings{nozza-hovy-2023-prof,
        title = "The State of Profanity Obfuscation in Natural Language Processing Scientific Publications",
        author = "Nozza, Debora  and
          Hovy, Dirk",
        booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
        year = "2023",
        publisher = "Association for Computational Linguistics",
        }


## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
