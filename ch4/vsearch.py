
def search4vowels(phrase:str) ->set:
    return set('aeiou').intersection(set(phrase))

def search4letter(phrase:str,letters:str = 'aeiou') ->set:
    return set(letetrs).intersection(phrase)
