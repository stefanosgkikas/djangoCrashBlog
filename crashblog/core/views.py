from django.shortcuts import render
from blog.models import Post

# view που τραβάει δεδομένα από την βάση και τα στέλνει σε σελίδα
def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html' ,  {'posts': posts})

# απλή view για σελίδες
def about(request):
    return render(request, 'core/about.html')