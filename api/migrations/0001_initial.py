# Generated by Django 2.2.5 on 2020-12-22 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('key', models.CharField(blank=True, max_length=256, null=True)),
                ('secret', models.CharField(blank=True, max_length=256, null=True)),
                ('token', models.CharField(blank=True, max_length=128, null=True)),
                ('refreshed_at', models.DateTimeField(blank=True, null=True)),
                ('parameters', models.TextField(blank=True, null=True)),
            ],
        ),
    ]