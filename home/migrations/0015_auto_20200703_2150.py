# Generated by Django 3.0.7 on 2020-07-03 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200703_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='productlist',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='home.Order'),
            preserve_default=False,
        ),
    ]
