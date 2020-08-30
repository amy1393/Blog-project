from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    commented_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve_comment(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return self.text