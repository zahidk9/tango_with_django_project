import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views': 25},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 45},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views': 22} ]
    
    django_pages= [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 53},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views': 35},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views': 35} ]
        
    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 45},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 87} ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64}, 
            'Django': {'pages': django_pages, 'views':64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16 }}
    
    #MORE CATS AND PAGES MUST BE ADDED ABOVE
    
    #Go through cats dic and add each category and then add all pages for each category
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
        
    # Print out the categories we have added.
        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print(f'- {c}: {p}')

#add page method used above
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    
#add cat method used above
def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

#execution starts here
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

    
    