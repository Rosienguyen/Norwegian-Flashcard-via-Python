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

def translate_norsk(source_text, source_lan = 'no', translated_to = 'en'): 
    """
    taking the souce text from the source language to translate into another lauguage
    """

    source_lan = "no" #no is the code for Norwegian(Bokmål) Language
    translated_to= "en" #en is the code for Engllish Language
    output = dict() #SimpleNamespace()

    translated_text = Translator().translate(source_text, src = source_lan, dest = translated_to)
    output_no= dict()
    output_en = dict()

    for ind, (l1, l2) in enumerate(zip(source_text.splitlines(), translated_text.text.splitlines())):
        output_no[ind + 1]= {l1, l2}
    
    return output_no #, output_en



def translate(source_text, source_lan = 'no', translated_to = 'en'): 
    """
    taking the souce text from the source language to translate into another lauguage
    """

    source_lan = "no" #no is the code for Norwegian(Bokmål) Language
    translated_to= "en" #en is the code for Engllish Language

    translated_text = Translator().translate(source_text, src = source_lan, dest = translated_to)
    output_no= dict()

    for ind, (l1, l2) in enumerate(zip(source_text.splitlines(), translated_text.text.splitlines())):
        output_no[ind + 1]= {l1: l2}
    
    return output_no #, output_en

def translate_to_csv(source_text, source_lan = 'no', translated_to = 'en'): 
    """
    taking the souce text from the source language to translate into another lauguage
    """

    source_lan = "no" #no is the code for Norwegian(Bokmål) Language
    translated_to= "en" #en is the code for Engllish Language

    translated_text = Translator().translate(source_text, src = source_lan, dest = translated_to)
    output_no= dict()

    for ind, (l1, l2) in enumerate(zip(source_text.splitlines(), translated_text.text.splitlines())):
        output_no[ind + 1]= {l1: l2}
    
    return output_no #, output_en

