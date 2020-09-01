# Generated by Django 3.1 on 2020-09-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('fecha', models.CharField(max_length=300)),
                ('titulo', models.CharField(max_length=300)),
                ('texto', models.TextField()),
            ],
        ),
    ]