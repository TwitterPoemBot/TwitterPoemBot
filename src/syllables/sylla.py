dictionaries=['mhyph.txt']
dicts = []
for d in dictionaries:
	f = open(d)
	words = {}
	count = 0
	for line in f:
		count += 1
		#count syllables
		#assume same syntax as the moby dictionary hyphenator
		syllables = line.count('\xa5') + 1
		word = line.replace('\xa5', '').strip().lower()
		words[word] = syllables
	dicts.append(words)
	print "Total word count: " + str(count)


def syllables(word):
	# first go through every dictionary 
	for d in dicts:
		if word in d:
			return d[word]
	# use heuristic if it's not in any dictionary
	if len(word)<3:
		return 1
	else:
		count = len(vowel.findall(word))
        if word[-1] == 'e' and not vowel.findall(word[-2]) and vowel.findall(word[-3]):
            count -= 1
        return count

