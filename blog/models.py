
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
        """
        Override the default save() method to automatically generate a unique slug
        based on the post title. This only runs when the slug field is empty, so
        manually-edited slugs are preserved.
        """
        # Only generate a slug if one doesn't already exist
        if not self.slug:
            # Convert the title into a URL-friendly string
            base_slug = slugify(self.title)
            slug = base_slug

            # Ensure the slug is unique by appending "-1", "-2", etc. if needed
            # itertools.count() creates an increasing sequence: 1, 2, 3, ...
            for i in itertools.count(1):
                # If no existing post uses this slug, stop and use it
                if not Post.objects.filter(slug=slug).exists():
                    break
                # Otherwise append a number and try again
                slug = f"{base_slug}-{i}"
            # Assign the unique slug to the model instance
            self.slug = slug
        # Call Django's original save() method to complete saving the object
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
