from django.contrib import admin
from .models import Article, Journalist, Review, Ebook, Profile, ProfileStatus

# Register your models here.
admin.site.register(Article)
admin.site.register(Journalist)

admin.site.register(Ebook)
admin.site.register(Review)

admin.site.register(ProfileStatus)
admin.site.register(Profile)
