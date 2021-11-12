from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Post
from .forms import PostForm
from django.utils import timezone


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
             post = form.save(commit=False)
             post.pub_date = timezone.now()
             form.save()
             return HttpResponseRedirect('/#testimonials')
    else:
        form = PostForm()
    return render(request, 'base.html', {'form': form, 'latest_post_list': latest_post_list,})
    
