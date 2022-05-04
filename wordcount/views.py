from ast import operator
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    wordDict = {}

    for word in wordList:
        word = word.lower().strip(' ,.?!/-')
        if len(word)==0:
            continue
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word]=1

    return render(request, 'count.html', {
        'fulltext': fulltext,
        'count': len(wordList),
        'data': sorted(wordDict.items(), key=lambda item: item[1], reverse=True)
    })