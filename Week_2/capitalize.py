def preLetterCase(str,letter):
    i=str.lower().find(letter.lower())
    if i==-1:
        return str.lower()
    w1=str[:i].lower()
    w2=str[i:].upper()
    return w1+w2
print(preLetterCase("CAtCHa", "a"))