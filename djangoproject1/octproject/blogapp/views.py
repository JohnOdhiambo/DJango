from django.shortcuts import get_object_or_404, render, redirect
from . models import Blogs, Categories, Comment
from django.db import models
from django.core.paginator import Paginator
from django.db.models import Q # helps to filter data based on two or more criteria

# Create your views here.

def blog(request):
    approved_blogs = Blogs.objects.filter(is_published=True)
    #Fetch blog categories and count the number of articles in each category
    blog_categories = Categories.objects.annotate(blog_count=models.Count('blogs'))
    recent_posts = Blogs.objects.filter(is_published=True).order_by('-date')[:5] #in ascending and limit to 5 records

    #Loop through and give a count of each approved blog 
    for blog in approved_blogs:
        blog.comment_count = blog.comment_set.filter(is_approved=True).count()
    blogs_per_page = 2
    paginator = Paginator(approved_blogs,blogs_per_page)
    page_number = request.GET.get('page')
    blogpaginator = paginator.get_page(page_number)

    context = {'blogs': blogpaginator, 'blog_categories': blog_categories, 'recent_posts':recent_posts} #Add a dictionary of various variables
    return render(request, 'blog.html', context)

def blog_details(request):
    return render(request, 'blog_details.html')

def post_detail(request, url):
    post = get_object_or_404(Blogs, url=url)
    comments = post.comment_set.filter(is_approved=True)
    blog_categories = Categories.objects.annotate(blog_count=models.Count('blogs'))
    recent_posts = Blogs.objects.filter(is_published=True).order_by('-date')[:5] #in ascending and limit to 5 records
    context = {'post': post, 'comments': comments, 'blog_categories': blog_categories, 'recent_posts': recent_posts} 
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        email =  request.POST['email']
        comment_instance = Comment(name=name, email=email, message=message, blog=post)
        comment_instance.save()
        return redirect('postdetail',url=url)
    
    return render(request, 'blog_details.html', context)

def search(request):
    if request.method == "POST":
        search_intent = request.POST['search_intent']
        results = Blogs.objects.filter(Q(is_published=True) & Q(title__icontains=search_intent))

        #Fetch blog categories and count the number of articles in each category
        blog_categories = Categories.objects.annotate(blog_count=models.Count('blogs'))
        recent_posts = Blogs.objects.filter(is_published=True).order_by('-date')[:5] #in ascending and limit to 5 records

        #Loop through and give a count of each approved blog 
        for blog in results:
            blog.comment_count = blog.comment_set.filter(is_approved=True).count()
        blogs_per_page = 2
        paginator = Paginator(results,blogs_per_page)
        page_number = request.GET.get('page')
        blogpaginator = paginator.get_page(page_number)

    context = {'blogs': blogpaginator, 'blog_categories': blog_categories, 'recent_posts':recent_posts} #Add a dictionary of various variables

    return render(request, 'blog.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')