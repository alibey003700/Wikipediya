import wikipedia
def malumot(text):
    wikipedia.set_lang("uz")
    result = wikipedia.summary(text)
    return result
# print(malumot("Kitob"))