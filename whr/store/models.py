from django.db import models
from django.utils import timezone
# Create your models here.//
class Unit(models.Model):
    title = models.CharField(max_length=100,verbose_name='Наименование',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Единица измерения'
        verbose_name_plural='Единицы измерения'
        ordering=['title',]


# Категории
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title',]

    # Поставщики
class Postav(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование компании',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['title', ]

# Причины списания
class Spis(models.Model):
    title = models.CharField(max_length=150, verbose_name='Причина списания', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Причина списания'
        verbose_name_plural = 'Причины списания'
        ordering = ['title', ]

# Подразделения
class Podraz(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название подразделения', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['title', ]

    # Подотчетники
class Fio(models.Model):
    title = models.CharField(max_length=150, verbose_name='Подотчетное лицо', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подочтетное лицо'
        verbose_name_plural = 'Подотчетные лица'
        ordering = ['title', ]

# Объекты
class Obct(models.Model):
    title = models.CharField(max_length=150, verbose_name='Объект', )
    podraz=models.ForeignKey(Podraz,verbose_name='Подразделение',on_delete=models.PROTECT)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['podraz','title', ]

class Nom(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', )
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

class Jurnal(models.Model):
    oper=models.IntegerField(verbose_name="Код операции")
    nomerdoc=models.CharField(max_length=50,verbose_name='Номер документа')
    datadoc=models.DateTimeField(verbose_name='Дата документа')
    postav=models.ForeignKey(Postav,verbose_name='Поставщик',on_delete=models.PROTECT)
    obct=models.ForeignKey(Obct,verbose_name='Объект',on_delete=models.PROTECT)
    podraz=models.ForeignKey(Podraz,verbose_name='Подразделение',on_delete=models.PROTECT)
    fio=models.ForeignKey(Fio,verbose_name='Подотчет',on_delete=models.PROTECT)
    spis=models.ForeignKey(Spis,blank=True,null=True,verbose_name='Причина списания',on_delete=models.PROTECT)
    summa=models.FloatField(verbose_name='Сумма',default=0)
    nds=models.IntegerField(verbose_name='НДС',default=20)
    summawithnds=models.FloatField(verbose_name='Сумма с НДС',default=0)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')



    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-datadoc', ]



class JurnalDoc(models.Model):

    oper=models.IntegerField(max_length=1,verbose_name='Операция')
    iddoc=models.ForeignKey(Jurnal,on_delete=models.PROTECT)
    title=models.ForeignKey(Nom,verbose_name='Наименование',on_delete=models.PROTECT)
    price=models.FloatField(verbose_name='Цена',default=0.0)
    kol = models.FloatField(verbose_name='Цена', default=0.0)
    podraz=models.ForeignKey(Podraz,on_delete=models.PROTECT,verbose_name='Подразделение')
    postav=models.ForeignKey(Postav,on_delete=models.PROTECT,verbose_name='Поставщик')
    obct=models.ForeignKey(Obct,on_delete=models.PROTECT,verbose_name='Объект')
    fio=models.ForeignKey(Fio,on_delete=models.PROTECT,verbose_name='Подотчетник')
    spis=models.ForeignKey(Spis,on_delete=models.PROTECT,null=True,blank=True,verbose_name='Причина списания')
    summa=models.FloatField(verbose_name='Сумма')
    nds=models.IntegerField(default=20,verbose_name='НДС')
    summawithnds=models.FloatField(verbose_name='Сумма с НДС')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Создан')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')
    uniqfield=models.CharField(max_length=250,verbose_name='Слаг')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Табличная часть'
        verbose_name_plural = 'Табличные части'
        ordering = ['-created_at', ]



