from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from models import Translation
import re
import urllib2
import json
import random

def main(request):
    return render(request, 'Translator/main.html', context_instance = RequestContext(request))

def translate(request):
    sourceText = request.GET['sourceText']
    if sourceText:
        translatedText = getTranslation(sourceText)
        storeTranslation(request, sourceText, translatedText)
        return HttpResponse(translatedText)
    else:
        response = "The text did not exist. If this problem continues, tell Tye!";
        httpBadRequest = 400
        return HttpResponse(response, httpBadRequest)
      
def getTranslation(sourceText):
    tokens = sourceText.split(' ')
    translatedTokens = [translateToken(token) for token in tokens]
    translatedText = ' '.join(translatedTokens)
    return translatedText

def storeTranslation(request, sourceText, translatedText):
    if request.user.is_authenticated():
        translation = Translation.create(request.user, sourceText, translatedText)
        translation.save()

def translateToken(token):
    match = re.match('\w+', token)
    if match:
        mainWord = match.group(0)
        translatedWord = getTranslatedWord(mainWord)
        token = token.replace(mainWord, translatedWord)
        
    return token
  
def getTranslatedWord(word):
    apiKey = 'd220bdc6acf296a3ae6a8b437cb881c4'
    url = "http://words.bighugelabs.com/api/2/%(apiKey)s/%(word)s/json" % {"apiKey": apiKey, "word": word}
    return getTranslationFromURL(url, word)
  
def getTranslationFromURL(url, word):
    request = urllib2.Request(url)
    translatedWord = word
    
    #No need to check for 303, since urlopen follows redirects
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError:
        #word does not exist in thesaurus
        pass
    else:
        body = response.read()
        print 'Request for %s' % word
        print body
        parsedResponse = json.loads(body)
        allRelatedWords = parsedResponse.values()
        wordPool = [word]
        for relatedWords in allRelatedWords:
            relatedWordsRelationTypes = ('syn', 'sim', 'usr')
            for relationType, wordList in relatedWords.iteritems():
                if relationType in relatedWordsRelationTypes:
                    wordPool.extend(wordList)

        translatedWord = random.choice(wordPool)
        if word == word.capitalize:
            translatedWord = translatedWord.capitalize 
    
    return translatedWord
    