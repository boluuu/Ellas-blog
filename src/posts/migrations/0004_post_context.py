# Generated by Django 3.1.2 on 2020-11-07 21:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='context',
            field=tinymce.models.HTMLField(default='Test'),
            preserve_default=False,
        ),
    ]
