from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
from .forms import PostForm
# Create your views here.
class listpost_view(ListView):
	model = Post
	template_name = 'post/listpost.html'

class detailpost_view(DetailView):
	model = Post
	template_name = 'post/detailpost.html'


class addpost_view(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'post/addpost.html'
	# fields = '__all__'
	# fields = ('title', 'body')
