# Generated by Django 3.0.7 on 2020-06-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200630_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
