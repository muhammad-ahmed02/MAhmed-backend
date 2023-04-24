from django.db import models
from froala_editor.fields import FroalaField


class Project(models.Model):
    name = models.CharField(max_length=64)
    details = FroalaField()
    image = models.URLField(max_length=225, blank=True, null=True)
    link = models.URLField(max_length=225, blank=True, null=True)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=24)
    details = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name


class About(models.Model):
    detail = FroalaField()

    def __str__(self):
        return self.detail


class Contact(models.Model):
    firstName = models.CharField(max_length=25, blank=True, null=True)
    lastName = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
