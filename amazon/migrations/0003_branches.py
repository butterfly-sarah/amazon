# Generated by Django 3.2.7 on 2021-09-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0002_rename_name_product_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
