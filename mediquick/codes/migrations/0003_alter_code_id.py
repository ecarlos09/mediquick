# Generated by Django 3.2.3 on 2021-05-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_code_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
