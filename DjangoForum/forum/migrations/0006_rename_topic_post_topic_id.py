# Generated by Django 4.0.1 on 2022-04-19 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_post_topic_id_post_topic_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='topic_id',
        ),
    ]