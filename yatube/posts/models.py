from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post'
    )
    group = models.ForeignKey(
        'Group',
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='group'
    )

    def __str__(self):
        return f'Post {self.pk}'


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'