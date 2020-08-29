from django.db import models


class Hero(models.Model):
    name = models.CharField(u"Name", max_length=50)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Heros"

    def __str__(self):
        return self.name
