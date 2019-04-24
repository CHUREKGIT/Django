from django.http import HttpResponse
from django.shortcuts import render
import collections

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    list_words = fulltext.split()
    count_word = len(list_words)
    popular = collections.Counter(list_words)
    
    for list in popular.most_common():
        word, number = zip(list)
        print(f"Word '{word[0]}' is in in your sentence {number[0]} times")
    
    # print(count_word)
    # print(popular.most_common())
    return render(request, 'count.html', {'fulltext': fulltext,'count_word': count_word, 'popular': popular.most_common()})

def about(request):
    return render(request, 'about.html')
