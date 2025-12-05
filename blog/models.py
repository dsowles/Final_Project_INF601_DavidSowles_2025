
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto-slug generation (your current implementation)
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            for i in itertools.count(1):
                if not Post.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
