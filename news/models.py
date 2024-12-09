from django.db import models
 
class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=255, default='title')
    text = models.TextField(default='пустой пост')

    def __str__(self):
        return self.title

