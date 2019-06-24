import re
import jieba


news_file = open('redbean.txt','r').read()
news = news_file.split('\n')[0]

tokens = jieba.cut_for_search(news)
print(', '.join(tokens))