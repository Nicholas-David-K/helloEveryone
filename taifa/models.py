from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.





#! API Articles -------------------------------------------------------


class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    author = models.ForeignKey(Journalist, 
                               on_delete=models.CASCADE,
                               related_name="articles")
    # author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.title}"




#! API Ebooks -------------------------------------------------------



class Ebook(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title




class Review(models.Model):
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)




#! THE USER PROFILE -------------------------------------------------------

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=240, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username



class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return f"{self.user_profile}"





