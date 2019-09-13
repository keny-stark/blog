from django.db import models
status_choices = [('New', 'new'), ('In progress', 'in progress'), ('Done', 'done')]


class Article(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Description')
    status = models.TextField(max_length=40, null=False, blank=False,
                              choices=status_choices, default='new', verbose_name='Status')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Text')
    created_at = models.DateField(auto_now=False, null=True, blank=True, verbose_name='Date of completion')
