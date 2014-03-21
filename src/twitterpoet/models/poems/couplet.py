from random import sample

def couplet(corpus):
    ''' Generates a Couplet poem given a list of (text, syllable count, rhyme) tuples ''' 

    def get_lines(phone):
        return [line for line in corpus if line != {} and line['phone'] == phone]
    def get_lines2():
	return [line for line in corpus if line != {} and len(get_lines(line['phone']))]  
    try:
        # Get random sample from 5 or 7 syllable tweets
        first = sample(get_lines2(), 1)
	phone = first[0]
	phone = phone['phone']
	second = first
	print len(get_lines(phone))
        if len(get_lines(phone)) > 1:
            while first == second:
                second = sample(get_lines(phone), 1)
	else:
	    raise Exception('Could not construct haiku - not enough tweets found')
    except ValueError as e:
        raise Exception('Could not construct haiku - not enough tweets found') 
    first = first[0]
    second = second[0]
    poem = [first['line']]
    poem += [second['line']]
    return '\n'.join(poem)