# Generated by Django 3.2.13 on 2022-06-18 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_alter_review_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='title',
        ),
    ]