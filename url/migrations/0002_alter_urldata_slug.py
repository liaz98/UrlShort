# Generated by Django 3.2 on 2021-05-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldata',
            name='slug',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]