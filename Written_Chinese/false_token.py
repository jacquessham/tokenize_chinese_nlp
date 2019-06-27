import re
from random import shuffle


opinion_file = open('written_chinese.txt','r').read()
opinion = opinion_file.split('\n')[0]
print('The original text is:\n',opinion, sep='')

sino_punc = open('sino_punc.txt','r').read()
opinion_cleaned = re.sub(sino_punc, '', opinion)
print('After removing punctuation:\n',opinion_cleaned, sep='')

tokens = list(opinion_cleaned)
shuffle(tokens)
output = '\n'.join(tokens[:5])

summ_file = open('summary_opinion.txt','w')
summ_file.write(output)
summ_file.close()