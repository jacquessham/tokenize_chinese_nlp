# Tokenize Chinese phrases from an Ancient Chinese Poem

## Background
The section of "Tokenizing individual Chinese characters of an ancient Chinese Poem" investigates how to tokenize Chinese Phrases by spliting individual Chinese words with Chinese poem written in 1000 years ago, or Tang Dynasty.

## Goal
There are 2 goals:
1. Unigram (Tokenize by Chinese words)
2.Tokenize using jieba (Did not mention in the Medium Post)

## Files
1. readbean.txt
2. summary_redbean.txt
<br><br>
The file "readbean.txt" contains:
* First line is the poem written in Chinese
* Line 2-5 are the English translation
* Line 6-7 are the Poem name in Chinese and English, respectively
* Line 8 is the url of the reference of the English translation
<br><br>
The file "summary_redbean.txt" is the result of "readbean.py" that is mentioned in the post.

## Codes
1. redbean.py
2. rebean_jieba_token.py
<br><br>
The file "redbean.py" splits the Chinese words and save as txt file.
<br><br>
The file "redbean_jieba_token.py" tokens Chinese phrases with jieba, but never mentioned in the post.
