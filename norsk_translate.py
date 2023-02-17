from googletrans import Translator
import pandas as pd

def translate_to_df(source_text, source_lan = 'no', translated_to = 'en') -> pd.DataFrame: 
    """
    taking the souce text from the source language to translate into another lauguage
    """

    source_lan = "no" #no is the code for Norwegian(Bokmål) Language
    translated_to= "en" #en is the code for Engllish Language

    translated_text = Translator().translate(source_text, src = source_lan, dest = translated_to)
    # Creating the DataFrame
    df = pd.DataFrame({'NO': source_text.splitlines(), 'EN': translated_text.text.splitlines()})
    return df

