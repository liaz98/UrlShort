# Generated by Django 3.2 on 2021-05-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0006_rename_slug_urldata_new_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='new_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
