from django.db import models
from django.contrib.auth.models import User

class StatusList(models.Model):
    name= models.TextField()
    color= models.TextField()

class Film(models.Model):
    name= models.TextField()
    originalname= models.TextField()
    status=models.ForeignKey(StatusList,default=1,on_delete=models.SET_DEFAULT)
    length= models.IntegerField()
    year=models.IntegerField()
    kinopoiskid= models.IntegerField()
    img= models.URLField(default="https://dummyimage.com/210x300/546de5/fff.png&text=Poster%20Not%20Found")
    rating= models.FloatField(default=0)
    disctiption= models.TextField(default="Нет данных")

    def get_absolute_url(self):
        return "/film/%i" % self.id

class Serial(models.Model):
    name= models.TextField()
    originalname= models.TextField()
    episodelength= models.IntegerField()
    year=models.IntegerField()
    kinopoiskid= models.IntegerField()
    img= models.URLField(default="https://dummyimage.com/210x300/546de5/fff.png&text=Poster%20Not%20Found")

    def get_absolute_url(self):
        return "/serial/%i" % self.id
    
class Season(models.Model):
    name= models.TextField()
    status=models.ForeignKey(StatusList,default=1,on_delete=models.SET_DEFAULT)
    episodecount= models.IntegerField()
    serial= models.ForeignKey(Serial,on_delete=models.CASCADE)
    disctiption= models.TextField(default="Нет данных")
    img= models.ImageField(upload_to='Seasons', default="default.png")
    rating= models.FloatField(default=0)

class SeriesList(models.Model):
    season= models.ForeignKey(Season,on_delete=models.CASCADE)
    name= models.TextField()
    date=models.DateField()

class GenreList(models.Model):
    name= models.TextField()

class Genre(models.Model):
    genre= models.ForeignKey(GenreList,on_delete=models.CASCADE)
    serial= models.ForeignKey(Serial,on_delete=models.CASCADE)

class GenreF(models.Model):
    genre= models.ForeignKey(GenreList,on_delete=models.CASCADE)
    film= models.ForeignKey(Film,on_delete=models.CASCADE)

class UserList(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    season= models.ForeignKey(Season,on_delete=models.CASCADE)
    serial= models.ForeignKey(Serial,on_delete=models.CASCADE)
    userrate= models.IntegerField(default=0)
    userstatus= models.IntegerField(default=1)
    userepisode= models.IntegerField(default=0)
    countreview= models.IntegerField(default=0)

class UserListF(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    film= models.ForeignKey(Film,on_delete=models.CASCADE)
    userrate= models.IntegerField(default=0)
    userstatus= models.IntegerField(default=1)
    countreview= models.IntegerField(default=0)