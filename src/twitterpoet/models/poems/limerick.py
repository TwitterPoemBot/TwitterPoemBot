from random import sample
import logging

def limerick(corpus):
    ''' Generates a limerick given a dictionary of line/syllables/phone ''' 

    def get_lines(sylla_min, sylla_max, n):
        ''' Returns dic of at least n rhyming tweets within the given syllable range
            ex. {'ha1':['some tweet text', 'some other text']} '''

        lines = [line for line in corpus if line['syllables'] >= sylla_min and line['syllables'] <= sylla_max] 
        logging.info(lines)
        dic = {}
        # dic is a dictionary of phone strings to line dictionaries
        for line in lines:
            phone = line['phone']
            if phone in dic:
                if line['last_word'] dic[phone]
                dic[phone].append(line)
            else:
                dic[phone] = [line]
        # Pick the least syllabically variant n lines
        return_lines = () # A tuple of (list of lines, variance)
        for key in dic:
            lines = dic[key]
            if len(lines) >= n:
                # Check variance, we want lines with similar syllable counts
                variance = max(lines, key=lambda line:line['syllables'])['syllables'] - \
                           min(lines, key=lambda line:line['syllables'])['syllables']

                if len(return_lines) == 0 or return_lines[1] > variance:
                    return_lines = ([line['line'] for line in lines], variance)
        if len(return_lines) != 0:
            return return_lines[0]
        else:
            raise ValueError

    '''
    6-12A
    6-12A
    3-6B
    3-6B
    6-10A
    '''
    try:
        a = get_lines(6, 12, 3) # Get 3 6-10 syllable lines that rhyme
        b = get_lines(3, 6, 2)  # Get 2 3-6 syllable lines that rhyme
    except ValueError as e:
        raise Exception('Could not construct limerick - not enough tweets') 

    poem = a[:2]
    poem += b
    poem += a[2:]
    return '\n'.join(poem)


