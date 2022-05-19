from django.db import models


# Create your models here.
class Tag(models.Model):
    text = models.CharField(max_length=255, blank=False, null=False, unique=True, primary_key=True)
    slug = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(max_length=1024, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["text", ]),
            models.Index(fields=["slug", ]),
        ]
        ordering = ["text" ,]

    def save(self, *args, **kwargs):
        self.slug = self.text.replace(" ", "-").lower()
        super().save(*args, **kwargs)
