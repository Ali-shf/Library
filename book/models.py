from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image', null=True, blank=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2  
    )
    publish_date = models.DateField()
    authors = models.ManyToManyField(to='Author')
    categories = models.ManyToManyField(to="Category")

    def __str__(self):
        return self.title





class User(AbstractUser):
        pass

        def __str__(self):
            return self.username



class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')


    def __str__(self):
            return f"{self.user.username} ❤️ {self.book.title}"



