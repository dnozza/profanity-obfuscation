<a href="https://colab.research.google.com/drive/1fXJjr_rwqvpp1IdNQ4dxqN4Dp88cxO97?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
[![arxiv.org](http://img.shields.io/badge/cs.CV-arXiv%3A2207.02696-B31B1B.svg)]([https://arxiv.org/abs/2207.02696](https://arxiv.org/abs/2210.07595))


# Profanity Obfuscation

[Debora Nozza](https://deboranozza.com/) · [Dirk Hovy](http://www.dirkhovy.com/)

Python package for obfuscating profanities, appeared in Findings of ACL 2023.

See the paper for additional details:

*Nozza, D., Hovy, D. "The State of Profanity Obfuscation in Natural Language Processing Scientific Publications". In Findings of the Association for Computational Linguistics: ACL 2023. Association for Computational Linguistics, 2023.* https://aclanthology.org/2023.findings-acl.240/


## Tutorial  
| Google Colab demo | 
|:-:|
|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fXJjr_rwqvpp1IdNQ4dxqN4Dp88cxO97?usp=sharing)|

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

       @inproceedings{nozza-hovy-2023-state,
    title = "The State of Profanity Obfuscation in Natural Language Processing Scientific Publications",
    author = "Nozza, Debora  and
      Hovy, Dirk",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.240",
    pages = "3897--3909",
    }


## Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
