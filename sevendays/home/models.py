from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    banner_title = models.CharField(max_length=100, default='Welcome to my homepage!')

    introduction = models.TextField(blank = True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    admin = models.ForeignKey(
        'Admin',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    body = StreamField([
        # ('name', blocks.somethingblock()),
        ('heading', blocks.CharBlock(template="heading_block.html")),
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'), 
        FieldPanel("introduction"),
        FieldPanel("banner_image"),
        FieldPanel("admin"),
        FieldPanel("body"),
    ]

@register_snippet
class Admin(models.Model):
    name = models.CharField(max_length = 100)
    title = models.CharField(blank=True, max_length= 100)
    company_name = models.CharField(blank=True, max_length= 100)
    company_url = models.URLField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+'
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("company_name"),
        FieldPanel("company_url"),
        FieldPanel("image"),
    ]

    def __str__(self):
       return self.name