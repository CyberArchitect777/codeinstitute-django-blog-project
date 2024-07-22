from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True) # The title value should be unique to avoid blog entries with the same name.
    slug = models.SlugField(max_length=200, unique=True) # Slug is an article that is still in production in the newspaper industry. In this case, it’ll store the URL of the article.
    author = models.ForeignKey(
	    User, on_delete=models.CASCADE, related_name="blog_posts"
    ) # One-to-many database relationship. Cascade on delete means that all posts are deleted if the user who writes them is deleted.
    excerpt = models.TextField(blank=True) # Is non-required
    content = models.TextField() # Blog article content
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
