import string
import random

def load_words():
    # WORDLIST_FILENAME ="words.txt"
    # infile=open("words.txt","r")
    # line=infile.readline()
    # word_list=string.split(line)
    # return (word_list)


    word_list = ["likhitha", "royal", "krishnalikhitha","laptop","suryanarayana","hangman","python",
    " random","restuarnt","navgurukul","all is well"]
    return word_list

def choose_word():
    # word_list=load_words()
    # secret_word=random.choice(word_list)
    # secret_word=secret_word.lower()
    # return secret_word
    
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word