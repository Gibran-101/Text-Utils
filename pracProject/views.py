




  

    



from distutils.util import change_root
from string import punctuation
from django.http import Http404, HttpResponse
from django.shortcuts import render
  

def index(request):
    # params ={'name':'Gibran','favColor':'teal'}
    return render(request, 'index.html')
    #  return HttpResponse('<button type="button"> <a href="http://127.0.0.1:1111/capitalize"> Homez </a> </button>')  
def analyze(request):
    djtext = request.POST.get('text','default')
    rempunc = request.POST.get('removepunc','off')
    capslock = request.POST.get('capslock','off')
    newLineRemover = request.POST.get('newLineRemover','off')
    RSR = request.POST.get('redundantSpaceRemover','off')
    CC = request.POST.get('charCount','off')


    if rempunc == "on":
        # analyzed = djtext
        punctuations = '''!()-{}.[];:'"\,<>?/?@#$%^&*~_=`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}   
        djtext = analyzed     
        # return render(request,'analyze.html',params)

    if(capslock == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UPPER CASE','analyzed_text': analyzed} 
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(newLineRemover == "on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(RSR == "on"):
        analyzed=""
        for index,char in  enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(CC == "on"):
        analyzed=""
        analyzed = len(djtext)
        params = {'purpose':'Removed new lines','analyzed_text': analyzed} 
        djtext = analyzed
        # return render(request,'analyze.html',params)

    if(rempunc != "on" and capslock != "on" and newLineRemover != "on" and RSR != "on" and CC != "on"):    
        return HttpResponse("Please select any one of the following operations!")

    return render(request,'analyze.html',params)

                             
