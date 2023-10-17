from django.db import models
"""
# Create your models here.
PRIORITY=[
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low'),
]
class Question(models.Model):
    title           =models.CharField(max_length=60)
    Question        =models.TextField(max_length=400)
    priority        =models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='The Question'#this is your row name under which all of your questions adds.
        verbose_name_plural='Peoples Question'#here this is your home table name under you app name
        """