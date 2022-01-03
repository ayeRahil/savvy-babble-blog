from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    articleImage = models.ImageField(upload_to='images/article/', default ='images/articledefault.jpg')
    title_tag = models.CharField(max_length=256, default='Technology')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=256, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
        #return reverse('article-detail', args= (str(self.id)))


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    authorImage = models.ImageField(upload_to = 'images/author/' , default='images/authordefault.jpg')
    instagram_url = models.CharField(max_length=500, blank=True)
    linkedin_url = models.CharField(max_length=500, blank=True)
    github_url = models.CharField(max_length=500, blank=True)
    twitter_url = models.CharField(max_length=500, blank=True)
    facebook_url = models.CharField(max_length=500, blank=True)
    mail_id = models.CharField(max_length=500, blank=True)
    

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='userComment', on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)