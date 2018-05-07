from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Category
#from .models import Image

#views
'''
def welcome(request):
    return HttpResponse('Pintrest')
    '''
'''
#pintresthomepageview
def welcome(request):
    return render(request, 'pintrest.html')
    '''

def welcome(request):
    profiles = Image.get_images()
    return render(request, 'welcome.html', {"profiles": profiles})


def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_categories = Image.search_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pinapps/search.html', {"message": message, "categories": searched_categories})

    else:
        message = "kindly search for and item"
        return render(request, 'all-pinapps/search.html', {"message": message})


def image(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-pinapps/image.html", {"image": image})
