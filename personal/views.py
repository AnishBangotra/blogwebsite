from django.shortcuts import render
from blog.models import BlogPost 
from operator import attrgetter
from blog.views import get_blog_queryset
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#whenever you work on your apps, their views and test all this is backened and frontend all html css in templates
# Create your views here.

BLOG_POSTS_PER_PAGE = 3

def home_screen_view(request):#request here is a type which is going to server
    context={}
    #context['some_string']="This is some string that i am passing to the view"
    #context['some_number']=12341
    #or you can do it like this
    #context={
     #   'some_string':"this is some string , im passing in the view",
      #  "some_number":123432,
    #}
    #list_of_values=[]
    #list_of_values.append('first entry')
    #list_of_values.append('second entry')
    #list_of_values.append('third entry')
    #list_of_values.append('fourth entry')

    query=""
    if request.GET:
        query=request.GET.get('q', '')
        context['query']=str(query)

    blog_posts= sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    #pagination
 
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts']=blog_posts
    return render(request, "personal/home.html", context)

  