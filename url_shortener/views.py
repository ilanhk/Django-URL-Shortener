from django.shortcuts import render
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string #to create random characters that are required for the url

# Create your views here.
def home(request):
    return render(request, 'create.html')

# To make Short URL
def generate_shortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_character_list = list(string.ascii_letters) # return all letters in the alphabet
            random_characters = ''

            # To create a 6 character url:
            for i in range(6):
                random_characters += random.choice(random_character_list) # to choose a random letter from the random_character_list

            time = datetime.now()
            short_url_obj = ShortURL(original_url= original_website, short_url= random_characters, time_dated_created= time)
            short_url_obj.save() # to save the object to the database

            return render(request, 'url_created.html',  {'chars':random_characters})

        else:
            form = CreateNewShortURL() #To give a blank form

            context = {
                'form': form
            }
            return render(request, 'create.html', context)

# To make sure the object exists
def redirect(request, url):
    url_specified = ShortURL.objects.filter(short_url= url)

    # To See if url exists
    if len(url_specified) == 0:
        return render(request, '404page.html')

    context = {
        'obj': url_specified[0]
    }

    return render(request, 'redirect.html', context)


