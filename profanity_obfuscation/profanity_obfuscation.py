import pandas as pd
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

    def reveal_profanity(self, profanity_obfuscated, lang="any"):
        """
        Predicts the emotion for the sentences in input
        @param profanity: profanity to be revealed
        @param lang: text's language
        @return: revealed profanity
        """

        if lang != "any":
            assert lang in ['EN', 'FR', 'DE', 'IT', 'ES']
            prof_table_lang = self.prof_table[self.prof_table['language'] == lang]
        else:
            prof_table_lang = self.prof_table

        profanity = prof_table_lang[prof_table_lang['obfuscation'] == profanity_obfuscated]['profanity']

        profanity = profanity.unique()[0]

        return profanity
