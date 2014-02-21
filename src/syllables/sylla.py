import re
dictionaries=['mhyph.txt']
dicts = []
vowel = re.compile(r'[aoiuy]+')

# Set-up
for d in dictionaries:
	f = open(d)
	words = {}
	for line in f:
		#count syllables
		#assume same syntax as the moby dictionary hyphenator
		syllables = line.count('\xa5') + 1
		word = line.replace('\xa5', '').strip().lower()
		words[word] = syllables
	dicts.append(words)

def syllables(word):
	''' Returns the number of syllables in the given word '''
	if word in words:
		return words[word]

	# use heuristic if it's not in any dictionary
	if len(word) <= 3:
		return 1
	else:
		count = len(vowel.findall(word))
        if word[-1] == 'e' and not vowel.findall(word[-2]) and vowel.findall(word[-3]):
            count -= 1
        return count

