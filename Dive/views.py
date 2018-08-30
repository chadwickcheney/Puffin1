import json, time
from django.shortcuts import render
from django.http import HttpResponse
from .models import Site
from .forms import SiteForm

def loading(request): #return dictionary for Site (all Pages) ajax
    master_dictionary = {}
    if request.is_ajax():
        form = SiteForm()
        print('ajax')
        if Site.objects.all():
            site = Site.objects.order_by()[0]
            print(site)
            master_dictionary = returnUrlData(site)
    data = json.dumps(master_dictionary)
    return HttpResponse(data)

def index(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        site = request.POST['address']
        print("length of request: " + str(len(str(site))) + " " + str(site))
        if len(str(site)) > 6 and 'htt' in str(site):
            if form.is_valid():
                if not Site.objects.filter(address=site):
                    print('\n!@#$\n')
                    form.save()
                #else:
                    #if found return old result
        else:
            #update html page to say format is incorrect
            print("Wrong format")

    #Restart the form
    form = SiteForm()
    sites = Site.objects.all()
    return render(request, 'dive.html', {'form':form}) #{}

def returnUrlData(url):
    time.sleep(2)
    return {"url1":"url"}
