from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    myself = {'name':"bibek"}
    return render(request, 'index.html', myself)

def about(request):
    return HttpResponse("This is a first project")

def result(request):
    
    data = request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    upper = request.POST.get('upper','off')
    space = request.POST.get('space','off')

    if removepunc == 'on':
        analyzed = ''
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in data:
            if char not in punctuation:
                analyzed = analyzed + char

        dictData={"result" : "Result", "takeData" : analyzed}
        data=analyzed

    if upper == "on":
        analyzed=''
        for char in data:
            analyzed = analyzed + char.upper()
        dictData={"result" : "Result", "takeData" : analyzed}
        data=analyzed

    if space == 'on':
        analyzed = ''
        for index, char in enumerate(data):
            if not (data[index] == ' ' and data[index + 1]== ' '):
                analyzed = analyzed + char

        dictData={"result" : "Result", "takeData" : analyzed}

    if (removepunc != 'on' and upper != "on" and space != 'on'):
        return HttpResponse("nothing clicked")
    return render(request, "result.html", dictData)
    
