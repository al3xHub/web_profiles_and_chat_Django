from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200)
    content = RichTextField(verbose_name="Content")
    order = models.SmallIntegerField(verbose_name="Order", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    class Meta:
        verbose_name = "web"
        verbose_name_plural = "websites"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
