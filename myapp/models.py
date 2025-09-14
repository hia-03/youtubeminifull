from django.db import models

from django.db import models

class User(models.Model):
    

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  
    image = models.ImageField(upload_to='images')
    agreed_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Post(models.Model):
    title=models.CharField( max_length=50)
    description=models.CharField( max_length=250)
    created_at=models.DateField( auto_now_add=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title