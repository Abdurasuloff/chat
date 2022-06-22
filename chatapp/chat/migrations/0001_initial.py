# Generated by Django 4.0.5 on 2022-06-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.CharField(default='&#10003;', max_length=150)),
            ],
        ),
    ]