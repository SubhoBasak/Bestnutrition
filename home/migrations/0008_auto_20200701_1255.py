# Generated by Django 3.0.7 on 2020-07-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200630_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='zip_code',
            new_name='pin_code',
        ),
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
        migrations.AddField(
            model_name='address',
            name='first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(1, 'Success'), (2, 'Pending')], default=1, max_length=1),
        ),
    ]
