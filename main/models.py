from django.db import models
import uuid

from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('shoes', 'Shoes'),
        ('jersey', 'Jersey'),
        ('accessories', 'Accessories'),
        ('ball', 'Ball'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    product_views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    @property
    def is_product_popular(self):
        return self.product_views > 50
        
    def increment_views(self):
        self.product_views += 1
        self.save()
