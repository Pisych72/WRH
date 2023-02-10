from django.db import models

# Create your models here.
class Unit(models.Model):
    title = models.CharField(max_length=100,verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Единица измерения'
        verbose_name_plural='Единицы измерения'
        ordering=['title',]


# Категории
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title',]