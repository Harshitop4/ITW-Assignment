from django.shortcuts import render, redirect
from .models import *

def home(request):
    if request.method == 'POST':

        data = request.POST

        long_url = data.get('long_url')
        print(long_url)
        # short_url = data.get('short_url')

        urlshortner.objects.create(
            long_url = long_url,
            # short_url = short_url
        )

        return redirect('/') 

    queryset = urlshortner.objects.all()

    context = {'urls':queryset}
    return render(request, 'home.html',context)
