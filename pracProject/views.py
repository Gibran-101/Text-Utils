from distutils.util import change_root
from string import punctuation
from django.http import Http404, HttpResponse
from django.shortcuts import render
  

def index(request):
    # params ={'name':'Gibran','favColor':'teal'}
    return render(request, 'index.html')
    #  return HttpResponse('<button type="button"> <a href="http://127.0.0.1:1111/capitalize"> Homez </a> </button>')  
def analyze(request):
    djtext = request.GET.get('text','default')
    rempunc = request.GET.get('removepunc','off')
    capslock = request.GET.get('capslock','off')
    newLineRemover = request.GET.get('newLineRemover','off')
    RSR = request.GET.get('redundantSpaceRemover','off')
    CC = request.GET.get('charCount','off')


    if rempunc == "on":
        # analyzed = djtext
        punctuations = '''!()-{}.[];:'"\,<>?/?@#$%^&*~_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}        
        return render(request,'analyze.html',params)

    elif(capslock == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UPPER CASE','analyzed_text': analyzed} 
        return render(request,'analyze.html',params)

    elif(newLineRemover == "on"):
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        return render(request,'analyze.html',params)

    elif(RSR == "on"):
        analyzed=""
        for index in  enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        return render(request,'analyze.html',params)

    elif(CC == "on"):
        analyzed=""
        analyzed = len(djtext)
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("error detected")  




  

    



# def capfirst(request):
#     return HttpResponse('<button type="button"> <a href="/"> this changes the case to capitalize </a> </button>')   
# def newLineRemover(request):
#     return HttpResponse("remove the redundant lines")  
# def spaceRemover(request):
#     return HttpResponse("remove the extra space") 
# def charCount(request):
#     return HttpResponse("count the number of characters in the string")                    