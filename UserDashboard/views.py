from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import RequestContext
from Translator.models import Translation
import operator

@login_required
def main(request):
    lastTenTranslations = getLastTenTranslations()
    topTenWords = getTopTenWordsFromLast100SourceTexts()
    print topTenWords
    context_instance = RequestContext(request, {'lastTenTranslations': lastTenTranslations, 'topTenWords': topTenWords})
    return render(request, 'UserDashboard/main.html',  context_instance)

def getLastTenTranslations():
    return Translation.objects.order_by('-id')[:10]

def getTopTenWordsFromLast100SourceTexts():
    last100Translations = Translation.objects.order_by('-id')[:100]
    last100SourceTexts = [translation.sourceText for translation in last100Translations]
    
    #TODO: Change this to a minheap to track top 100. Slightly worse performance, but much better memory use
    tokenToFrequency = {}
    
    for sourceText in last100SourceTexts:
        tokens = sourceText.split()
        for token in tokens:
            if token in tokenToFrequency:
                tokenToFrequency[token] += 1
            else:
                tokenToFrequency[token] = 1
        
    
    sortedTuples = sorted(tokenToFrequency.iteritems(), key=operator.itemgetter(1), reverse=True)  
    return sortedTuples[:10]
