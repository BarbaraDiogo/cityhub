# Generated by Django 5.0.3 on 2024-05-24 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_cityhub', '0004_alter_progress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='correlation',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='correlation',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Correlation',
        ),
    ]
