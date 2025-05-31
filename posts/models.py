from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#?  
class Status(models.Model):
    name = models.CharField(max_length=64)               #* Name of the status
    description = models.CharField(max_length=256)        #* Description of the status
    
    def __str__(self):
        return self.name                                 #* String representation of the status, returns the name


#? Post model definition
class Post(models.Model):
    title = models.CharField(max_length=128)             #* Title of the post
    subtitle = models.CharField(max_length=256)          #* Subtitle of the post
    body = models.TextField()                            #* Body content of the post
    
    author = models.ForeignKey(                          #* Foreign key relationship to the user model
        get_user_model(),                                #* Get the user model dynamically
        on_delete=models.CASCADE                         #* If the user is deleted, delete the post
    )
    
    status = models.ForeignKey(                          #* Foreign key relationship to the Status model
        Status,                                          #* Status model for the post
        on_delete=models.CASCADE,                        #* If the status is deleted, delete the post
    )
    
    created_on = models.DateTimeField(auto_now_add=True) #* Automatically set the date and time when the post is created
    
    #? returns a string representation of the post 
    def __str__(self):
        return self.title                                #* String representation of the post, returns the title
    
    #? gets the absolute URL for the post detail view 
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])         #* Returns the absolute URL for the post detail view, using the post's ID