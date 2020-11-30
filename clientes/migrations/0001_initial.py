# Generated by Django 3.1.3 on 2020-11-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=500, verbose_name='Endereço')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('data_cadastro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
