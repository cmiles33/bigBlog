# Generated by Django 4.0.1 on 2022-02-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0008_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorydata',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
