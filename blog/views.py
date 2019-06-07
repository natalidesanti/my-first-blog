from django.shortcuts import render
from django.utils import timezone
from .models import Post #Dot before models means current directory

# Creating my views here:

#This function receives a request and mount our model according to template 'blog/post_list.html'
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
