# Generated by Django 3.0 on 2024-02-09 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Score_Search', '0002_auto_20240209_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescore',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
