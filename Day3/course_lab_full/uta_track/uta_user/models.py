from django.db import models
from django.conf import settings

# Create your models here.

class Route(models.Model):
    route_number = models.CharField(max_length=20)
    route_name = models.CharField(max_length=30)

    def __str__(self):
        return self.route_name
    
class UtaUser(models.Model):
    favorite_route = models.CharField(max_length=30,blank=True)
    my_routes = models.ManyToManyField(Route, related_name='my_routes')
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    def __str__(self):
        return self.auth_user.username

class FaqMain(models.Model):
    active = models.BooleanField(unique=True)
    welcome_text = models.TextField()

    def __str__(self):
        return self.welcome_text

class Faq(models.Model):
    faq_text = models.TextField()
    faq_main = models.ForeignKey(FaqMain,on_delete=models.CASCADE)

    def __str__(self):
        return self.faq_text

class Comment(models.Model):
    comment = models.TextField()
    uta_user = models.ForeignKey(UtaUser,on_delete=models.CASCADE)
    def __str__(self):
        return f"user:{self.uta_user} {self.comment}"