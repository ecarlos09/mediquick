# Generated by Django 3.1 on 2021-05-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0003_alter_code_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]