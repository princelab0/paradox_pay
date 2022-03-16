# Generated by Django 4.0.2 on 2022-02-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products')),
                ('description', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
