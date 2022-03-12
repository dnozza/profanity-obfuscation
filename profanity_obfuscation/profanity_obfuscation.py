import pandas as pd
import functools
import re

class Prof:

    def __init__(self):
        """
        Class initialization
        """

        self.prof_table = pd.read_csv("resources/prof_table.tsv", sep="\t")

    def obfuscate_string(self, text, lang="any"):
        """
        Predicts the emotion for the sentences in input
        @param text: text to be obfuscated
        @param lang: text's language
        @return: obfuscated text
        """

        if lang != "any":
            assert lang in ['EN', 'FR', 'DE', 'IT', 'ES']
            prof_table_lang = self.prof_table[self.prof_table['language'] == lang]
        else:
            prof_table_lang = self.prof_table
        replacements = prof_table_lang[['profanity', 'obfuscation']].to_numpy()
        for k,v in replacements:
            text = re.sub(f'(?<![a-zA-Z]){k}(?![a-z-Z])', v, text)

        return text
