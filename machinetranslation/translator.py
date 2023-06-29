from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source="en", target="fr")
    translation = translator.translate(englishText)
    print(translation)
    return translation



    


    