# Generated by Django 3.0.7 on 2020-07-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20200704_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-order_date_time',)},
        ),
        migrations.AddField(
            model_name='order',
            name='oid',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
