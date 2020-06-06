
import requests
import string
from lxml import html
from googleSearch import googleSearch
from bs4 import BeautifulSoup
import random

# to search


def chatbot_query(query, index=0):
    fallback = 'Sorry, I cannot think of a reply for that.'
    result = ''

    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
    GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

    def greeting(sentence):
        """If user's input is a greeting, return a greeting response"""
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)

    if query[3:-1] in GREETING_INPUTS:
        print("here")
        return random.choice(GREETING_RESPONSES)
    try:
        search_result_list = googleSearch(query)
        print(search_result_list)
        page = requests.get(search_result_list[index])
        tree = html.fromstring(page.content)
        soup = BeautifulSoup(page.content, features="lxml")
        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback

        return result
    except:
        if len(result) == 0: result = fallback
        return result

