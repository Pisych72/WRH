# Generated by Django 3.0.8 on 2023-02-15 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_fio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Наименование')),
                ('srok', models.IntegerField(blank=True, default=0)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Создан')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Category', verbose_name='Категория')),
                ('izm', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Unit', verbose_name='Ед.изм.')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Номенклатура',
                'ordering': ['title'],
            },
        ),
    ]
