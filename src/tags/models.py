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

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.text = f"{str(self.text[0]).upper()}{self.text[1:]}"
            self.slug = str(self.text).replace(" ", "-").lower()
        super().save(*args, **kwargs)
