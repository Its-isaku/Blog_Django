

#? impoert necessary modules
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView,
) 
from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#? |-------------------------------------------------posts List------------------------------------------------| 
class PostListView(ListView):
    template_name = "posts/list.html"                                                   #* Template for listing posts
    model = Post                                                                        #* Model to be listed
    
    def get_context_data(self, **kwargs):                                               #* Get the context data for the template
        context =  super().get_context_data(**kwargs)                                   #* Get the default context data
        published = Status.objects.get(name="published")                                #* Get the "Published" status from the Status model
        
        context["title"] = "Published"                                                  #* Set the title for the context data
        context["post_list"] = (
            Post.objects                                                                #* Query the Post model to get all posts
            .filter(status=published)                         #* Filter posts by "Published" status
            .order_by("created_on").reverse()                                           #* Filter posts by "Published" status and order by creation date
        )       
        return context                                                                  #* Return the updated context data for the template
    
class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"                                                   #* Template for listing draft posts
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                    #* Get the default context data
        draft = Status.objects.get(name="draft")                                        #* Get the "Draft" status from the Status model
        
        context["title"] = "Draft"                                                      #* Set the title for the context data
        context["post_list"] = (
            Post.objects                                                                #* Query the Post model to get all posts
            .filter(author=self.request.user,status=draft)                              #* Filter posts by "Draft" status
            .order_by("created_on").reverse()                                           #* Order posts by creation date  
        )
        return context                                                                  #* Return the updated context data for the template
    
class PostArchiveListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                                    #* Get the default context data
        archived = Status.objects.get(name="archived")                                  #* Get the "Archived" status from the Status model
        context["title"] = "Archived"                                                   #* Set the title for the context data
        context["post_list"] = (
            Post.objects                                                                #* Query the Post model to get all posts
            .filter(author=self.request.user,status=archived)                           #* Filter posts by "Draft" status
            .order_by("created_on").reverse()                                           #* Order posts by creation date  
        )
        return context

#? |-----------------------------------------------Create a post-----------------------------------------------| 
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/create.html"                                                 #* Template for creating a post
    model = Post                                                                        #* Model to be created
    fields = ["title", "subtitle", "body", "status"]                                    #* Fields to be filled in when creating a post
    success_url = reverse_lazy("list")                                                  #* URL to redirect to after successful creation 
    
    def form_valid(self, form):
        form.instance.author = self.request.user                                        #* Set the author of the post to the current user
        return super().form_valid(form)                                                 #* Call the parent class's form_valid method to save the form and redirect 
        

#? |-----------------------------------------------details List------------------------------------------------| 
class PostDetailView(UserPassesTestMixin, DetailView):
    template_name = "posts/detail.html"                                                 #* Template for post details
    model = Post                                                                        #* Model to be detailed
    
    def test_func(self):
        post = self.get_object()                                                        #* Get the post object being detailed
        if post.status.name == "published":                                             #* Check if the post status is "Published"
            return True                                                                 #* Allow access if the post is published
        elif post.status.name == "archived" and self.request.user.is_authenticated:     #* Allow access if the post is archived and the user is authenticated
            return True                                                                 #* Allow access if the post is archived and the user is authenticated
        elif post.status.name == "draft" and self.request.user == post.author:
            return True                                                                 #* Deny access if the post is in draft status and the user is not the author or not authenticated
        else:
            return False                                                                #* Deny access if the post is not published, archived, or the user is not authenticated

#? |----------------------------------------------Updates a post-----------------------------------------------| 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"                                                   #* Template for editing a post
    model = Post                                                                        #* Model to be edited
    fields = ["title", "subtitle", "body", "status"]                                    #* Fields to be edited  
    success_url = reverse_lazy("list")                                                  #* URL to redirect to after successful update

    def test_func(self):
        post = self.get_object()                                                        #* Get the post object being edited
        return self.request.user == post.author                                         #* Check if the current user is the author of the post

#? |-----------------------------------------------Deletes a post-----------------------------------------------|
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"                                                 #* Template for deleting a post
    model = Post                                                                        #* Model to be deleted
    success_url = reverse_lazy("list")                                                  #* URL to redirect to after successful deletion 
    
    def test_func(self):
        post = self.get_object()                                                        #* Get the post object being deleted
        return self.request.user == post.author                                         #* Check if the current user is the author of the post