from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    users = models.CharField('Бренд', max_length=18)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"
