# Generated by Django 4.2.6 on 2024-04-03 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Retsept nomi')),
                ('content', models.TextField(verbose_name='Matni')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan vaqti')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqti")),
                ('photo', models.ImageField(upload_to='', verbose_name='Rasmi')),
                ('views', models.IntegerField(default=0, verbose_name="Ko'rishlar soni")),
                ('published', models.BooleanField(default=True, verbose_name='Saytga chiqarish')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.category', verbose_name='Kategoriya')),
            ],
        ),
    ]
