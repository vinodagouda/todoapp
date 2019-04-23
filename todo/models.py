from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ToDoDetails(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    
    # It is for representational puropose. Sample example below.
    # from todo.models import ToDoDetails
    # ToDoDetails.objects.all()
    # <QuerySet [<ToDoDetails: sameer,python>]>
    def __str__(self):
        return ('%s,%s')% (self.user.username, self.title)

