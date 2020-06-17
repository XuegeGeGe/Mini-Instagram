from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField


class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])


class InstaUser(AbstractUser):
    email_address = models.TextField(blank=True, null=True)
    profile_pic = ProcessedImageField(
        upload_to='static/images/users',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return 'Like: ' + self.user.username + '->' + self.post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(InstaUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return 'Comment: ' + self.user.username + '->' + self.post.title + ': ' + self.comment
