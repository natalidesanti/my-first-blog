from django.shortcuts import render

# Creating my views here:

#This function receives a request and mount our model according to template 'blog/post_list.html'
def post_list(request):
    return render(request, 'blog/post_list.html', {})
