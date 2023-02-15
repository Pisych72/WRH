from django.db import models

# Create your models here.
class Unit(models.Model):
    title = models.CharField(max_length=100,verbose_name='Наименование',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Единица измерения'
        verbose_name_plural='Единицы измерения'
        ordering=['title',]


# Категории
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование категории',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title',]

    # Поставщики
class Postav(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование компании', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['title', ]

# Причины списания
class Spis(models.Model):
    title = models.CharField(max_length=150, verbose_name='Причина списания', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Причина списания'
        verbose_name_plural = 'Причины списания'
        ordering = ['title', ]

# Подразделения
class Podraz(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название подразделения', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['title', ]

    # Подотчетники
class Fio(models.Model):
    title = models.CharField(max_length=150, verbose_name='Подотчетное лицо', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подочтетное лицо'
        verbose_name_plural = 'Подотчетные лица'
        ordering = ['title', ]

# Объекты
class Obct(models.Model):
    title = models.CharField(max_length=150, verbose_name='Объект', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['title', ]

class Nom(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', unique=True)
    izm=models.ForeignKey(Unit,verbose_name='Ед.изм.',on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    srok=models.IntegerField(blank=True,default=0)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'
        ordering = ['title', ]