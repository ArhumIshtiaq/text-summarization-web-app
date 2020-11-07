from nltk.tokenize import sent_tokenize
from preprocessing import preprocess
from summarize import summarize 
import bs4 as bs
import urllib.request
import re

def main():

    source = input('press 1 for link or 0 for a file:')
    if source == '1':
        scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
        article = scraped_data.read()

        parsed_article = bs.BeautifulSoup(article,'lxml')

        paragraphs = parsed_article.find_all('p')

        text = ""

        for p in paragraphs:
            text += p.text
    else:


        file = 'sample.txt'
        file = open(file , 'r')
        text = file.read()

    tokenized_sentence = sent_tokenize(text)
    tokenized_words = preprocess(text)
    summary = summarize(tokenized_words, tokenized_sentence)

    print("\n")
    print("Summary:")

    print(summary)
    outF = open('summary.txt',"w")
    outF.write(summary)

main()