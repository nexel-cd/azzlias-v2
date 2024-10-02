from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # New image field

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional discount field
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    fabric_type = models.CharField(max_length=100, choices=[
        ('cotton', 'Cotton'),
        ('silk', 'Silk'),
        ('linen', 'Linen'),
        ('polyester', 'Polyester'),
    ])
    sizes = models.ManyToManyField(Size, related_name='products', blank=True)  # Many-to-many relationship for sizes
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=0)
    amazon_affiliate_link = models.URLField(('Amazon'),blank=True, null=True)  # Optional field for affiliate links
    meesho_affiliate_link = models.URLField(('Meesho'),blank=True, null=True)  # Optional field for affiliate links
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"

class BestSeller(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(blank=True, null=True)  # Allow blank rank

    class Meta:
        ordering = ['rank']
        verbose_name_plural = "Best Sellers"

    def clean(self):
        # Automatically assign rank if not provided
        if self.rank is None:
            existing_ranks = BestSeller.objects.values_list('rank', flat=True)
            self.rank = max(existing_ranks, default=0) + 1  # Auto-increment rank

    def save(self, *args, **kwargs):
        # Call the clean method before saving to ensure rank is assigned
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - Rank {self.rank}"