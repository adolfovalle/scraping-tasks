# Generated by Django 3.1 on 2020-09-01 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('n_followers', models.IntegerField()),
                ('n_followees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediaid', models.IntegerField()),
                ('date_utc', models.DateTimeField()),
                ('caption', models.TextField(blank=True, null=True)),
                ('video_view_count', models.IntegerField(blank=True, null=True)),
                ('likes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.profile')),
            ],
        ),
    ]