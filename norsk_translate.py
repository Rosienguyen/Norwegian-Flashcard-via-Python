from googletrans import Translator
import pandas as pd


def translate_to_df(source_text,  translated_to = 'en') -> pd.DataFrame:
    """
    taking the souce text from the source language to translate into another lauguage
    """

    translated_text = Translator().translate(source_text, translated_to)
    # Creating the DataFrame
    df = pd.DataFrame({'NO': source_text.splitlines(), 'EN': translated_text.text.splitlines()})
    return df


