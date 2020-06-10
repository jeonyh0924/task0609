from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

User = get_user_model()


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    created = models.DateField(auto_now_add=True, )
    price = models.IntegerField()

    owner = models.ForeignKey(User, related_name='snippets', on_delete=models.CASCADE, null=True, )

    @staticmethod
    def start():
        for i in range(10):
            Snippet.objects.create(
                title=f'title is {i} index',
                code=f'code is {i}'
            )
