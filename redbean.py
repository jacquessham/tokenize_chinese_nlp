import re
from random import shuffle


redbean_file = open('redbean.txt','r').read()
redbean = redbean_file.split('\n')[0]
print('The original text is:\n',redbean, sep='')

sino_punc = open('sino_punc.txt','r').read()
redbean_cleaned = re.sub(sino_punc, '', redbean)
print('After removing punctuation:\n',redbean_cleaned, sep='')

tokens = list(redbean_cleaned)
shuffle(tokens)
output = '\n'.join(tokens[:5])

summ_file = open('summary_redbean.txt','w')
summ_file.write(output)
summ_file.close()
