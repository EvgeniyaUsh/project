from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
CHOICES_APPLICATION_SUBJECT = (
    ('test', 'Тест драйв'),
    ('question', 'Консультация'),
)


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    header = models.CharField(max_length=255)
    text = models.TextField()
    like = models.ManyToManyField(User, related_name='blog_post')

    objects = models.Manager()

    def likes_counter(self):
        return self.like.count()

    def __str__(self):
        return self.header
