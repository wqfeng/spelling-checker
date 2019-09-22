"""
Use a Markov Chain to do spelling-check.

>>> m = Markov("ab")
>>> m.predict("a")
>>> 'b'

"""
import random
import urllib.request as req

class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)
    
    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
            raise KeyError("no valid target")
        possibles = []
        for k, v in options.items():
            for i in range(v):
                possibles.append(k)
                
        return random.choice(possibles)

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data  = fin.read()
    fout = open(fname, 'wb')
    fout.write(data)
    fout.close()

def from_file(fname):
    with open(fname, 'r') as f:
        txt = f.read()
        return Markov(txt)
        

def get_table(txt):
    """ Build the transition table.

    >>> get_table("ab")
    >>> {'a': {'b': 1}}

    """
    results = {}
    for i in range(len(txt)):
        char = txt[i]
        try:
            out = txt[i + 1]
        except IndexError:
            break
        if char in results:
            char_dict = results[char]
        else:
            char_dict = {}
        if out not in char_dict:
            char_dict[out] = 0
        char_dict[out] += 1

        results[char] = char_dict
    return results
