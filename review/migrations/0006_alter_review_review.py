# Generated by Django 3.2.13 on 2022-06-18 05:02

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20220617_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=markdownx.models.MarkdownxField(),
        ),
    ]