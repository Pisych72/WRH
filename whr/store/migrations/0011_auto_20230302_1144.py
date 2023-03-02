# Generated by Django 3.0.8 on 2023-03-02 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_obct_podraz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obct',
            name='podraz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Podraz', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
    ]