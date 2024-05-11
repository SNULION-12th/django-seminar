# Generated by Django 5.0.4 on 2024-05-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_like_post_like_users'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='tag.tag'),
        ),
    ]
