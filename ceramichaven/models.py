from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class CeramicCollection(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'ceramic category'
        verbose_name_plural = 'ceramic categories'

    def get_absolute_url(self):
        return reverse('ceramichaven:selected_catalog',
                       args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(CeramicCollection,
                                 related_name='ceramic_products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.FileField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def get_absolute_url(self):
        return reverse('ceramichaven:product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name


class CollectionBlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    main_picture = models.FileField()
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256,
                            unique_for_date='publish')
    category = models.ForeignKey(CeramicCollection,
                                 on_delete=models.PROTECT,
                                 related_name='blog_display')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

