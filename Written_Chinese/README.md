# Tokenizing Chinese Phrases of a Hong Kong News Article

## Background
The section of "Tokenizing individual Chinese characters of a Hong Kong news article" and "Using the package jieba to tokenize" investigate how and why to tokenize Chinese Phrases with jieba.

## Files
1. summary_opinion.txt
2. written_chinese.txt
<br><br>
The file "summary_opinion.txt" is the result of "false_token.py" that is mentioned in the post.
<br><br>
The file "written_chinese.txt" contains 2 lines.<br>
Line 1 is the news passage.

## Codes
1. false_token.py
2. token852post.py
<br><br>
The file "false_token.py" split Chinese words from news passage to show unigram is not working in modern Chinese written. The result is save as txt file.
<br><br>
The file "token852post.py" tokens Chinese phrases with jieba, it does not save the result but print out.
