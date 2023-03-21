# Generated by Django 3.0.8 on 2023-03-10 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20230310_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurnal',
            old_name='total',
            new_name='summa',
        ),
        migrations.RenameField(
            model_name='jurnal',
            old_name='totalwithnds',
            new_name='summawithnds',
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='fio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Fio', verbose_name='Подотчет'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='obct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Obct', verbose_name='Объект'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='podraz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Podraz', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='jurnal',
            name='postav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Postav', verbose_name='Поставщик'),
        ),
    ]