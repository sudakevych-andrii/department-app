# Generated by Django 3.2 on 2021-04-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20210421_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]