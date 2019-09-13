# Generated by Django 2.2 on 2019-09-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')], max_length=3000, verbose_name='Description')),
                ('status', models.TextField(default='new', max_length=40, verbose_name='Status')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Date of completion')),
            ],
        ),
    ]
