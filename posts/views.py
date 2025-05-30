

#? impoert necessary modules
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
) 
from .models import Post
from django.urls import reverse_lazy

#? |----------------posts List----------------| 
class PostListView(ListView):
    template_name = "posts/list.html"                        #* Template for listing posts
    model = Post                                             #* Model to be listed

#? |----------------Create a post----------------| 
class PostCreateView(CreateView):
    template_name = "posts/create.html"                      #* Template for creating a post
    model = Post                                             #* Model to be created
    fields = ["title", "subtitle", "body", "author"]         #* Fields to be filled in when creating a post
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful creation 


#? |----------------Updates a post----------------| 
class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"                        #* Template for editing a post
    model = Post                                             #* Model to be edited
    fields = ["title", "subtitle", "body", "author"]         #* Fields to be edited  
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful update


#? |----------------Deletes a post----------------|
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"                      #* Template for deleting a post
    model = Post                                             #* Model to be deleted
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful deletion 