from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    return render(request ,'home.html', {})

def contact_page(request):
    return HttpResponse('<h1>This is contact page</h1> <br> <p>Contact Us</p>')

def count(request):
    data = request.GET['fultextarea']
    word_list = data.split()
    list_length = len(word_list)

    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1
        
    sorted_list = sorted(worddictionary.items())

    return render(request ,'count.html',{'fultext':data, 'words':list_length, 'worddictionary':sorted_list})

def aboutpage(request):
    Title = 'Hi Rikit' 
    return render(request,'about.html',{'Title':Title})