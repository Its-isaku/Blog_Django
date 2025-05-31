

#? impoert necessary modules
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
) 
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#? |----------------posts List----------------| 
class PostListView(ListView):
    template_name = "posts/list.html"                        #* Template for listing posts
    model = Post                                             #* Model to be listed

#? |----------------Create a post----------------| 
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/create.html"                      #* Template for creating a post
    model = Post                                             #* Model to be created
    fields = ["title", "subtitle", "body", "status"]         #* Fields to be filled in when creating a post
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful creation 
    
    def form_valid(self, form):
        form.instance.author = self.request.user             #* Set the author of the post to the current user
        return super().form_valid(form)                      #* Call the parent class's form_valid method to save the form and redirect 

#? |----------------details List----------------| 
class PostDetailView(DetailView):
    template_name = "posts/detail.html"                      #* Template for post details
    model = Post                                             #* Model to be detailed

#? |----------------Updates a post----------------| 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"                        #* Template for editing a post
    model = Post                                             #* Model to be edited
    fields = ["title", "subtitle", "body", "status"]         #* Fields to be edited  
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful update

    def test_func(self):
        post = self.get_object()                             #* Get the post object being edited
        return self.request.user == post.author              #* Check if the current user is the author of the post

#? |----------------Deletes a post----------------|
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"                      #* Template for deleting a post
    model = Post                                             #* Model to be deleted
    success_url = reverse_lazy("list")                       #* URL to redirect to after successful deletion 
    
    def test_func(self):
        post = self.get_object()                             #* Get the post object being deleted
        return self.request.user == post.author              #* Check if the current user is the author of the post