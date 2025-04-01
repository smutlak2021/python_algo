import re

def matchSyllable(syll, word):
    prefix = syll[0]
    cnt = syll[1]
    suffix = syll[2]

    if(len(prefix)>0 and len(suffix)>0):
        pattern = rf"{prefix.lower()}(.+?){suffix.lower()}"  # Use raw string for better readability
        match = re.search(pattern, word.lower())
    
        if match:
            if len(match.group(1)) == int(cnt):
                return True
    elif len(word) == int(cnt):
        return True
    
    return False

def convert_to_syllables(patt):

    pattern = r'(\d+)'
    arr = re.split(pattern, patt)

    numsIndexes =[]
    for index, a in enumerate(arr):
        if a.isnumeric() == True:
            numsIndexes.append(index)
    

    ret = []
    for b in numsIndexes:
        if(b>0):
            syllable = (arr[b-1] , arr[b] , arr[b+1])
            ret.append(syllable)

    return ret

def word_match(patt, word):
    print(patt+' '+word + ' --> ', end=" ")
    Syllables = convert_to_syllables(patt)
    for syll in Syllables:
        if not matchSyllable(syll, word):
            return False
    return True



print(word_match('F2eb2k', 'Facebook'))
print(word_match('i11l', 'International'))
print(word_match('8', 'facebook'))
print(word_match('F2eb5k', 'facebook'))