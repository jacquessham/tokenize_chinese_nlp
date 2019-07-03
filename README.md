# NLP - Tokenize Chinese Phrases

## Background
This github contains codes which are supplement to my <a href="https://medium.com/@jjsham/nlp-tokenizing-chinese-phases-3302da4336bf?source=friends_link&sk=6593b621ad75d7b0d52c48623740088c">Medium Post</a> related to tokenizing Chinese phrases.
<br>
<br>
This Github contains 3 folders related to 3 major sections in the post:<br>
1. Poem
2. Written Chinese
3. Cantonese
<br>
Note: Chinese words does not mean Chinese phrases. Chinese word means one Chinese characters, while Chinese phrases are phrases that make up with one or more characters.
<br>

## Poem
The section of "Tokenizing individual Chinese characters of an ancient Chinese Poem" investigates how to tokenize Chinese Phrases by spliting individual Chinese words with Chinese poem written in 1000 years ago, or Tang Dynasty:
1. Unigram (Tokenize by Chinese words)
2. Tokenize using jieba (Did not mention in the Medium Post)
<br><br>
You may find the related codes by going to the folder by clicking [here](/Poem)

## Written Chinese
The section of "Tokenizing individual Chinese characters of a Hong Kong news article" and "Using the package jieba to tokenize" investigate how and why to tokenize Chinese Phrases with jieba.
<br><br>
You may find the related codes by going to the folder by clicking [here](/Written_Chinese)

## Cantonese
The section of "How about Cantonese?" investigates the performance of jieba on written Cantonese.
<br><br>
You may find the related codes by going to the folder by clicking [here](/Cantonese)

## Files
* sino_punc.txt
This file contains all punctuation of Chinese, for regex.