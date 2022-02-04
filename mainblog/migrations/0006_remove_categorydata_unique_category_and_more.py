# Generated by Django 4.0.1 on 2022-02-03 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0005_categorydata_unique_category'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='categorydata',
            name='unique_category',
        ),
        migrations.RemoveField(
            model_name='categorydata',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to='mainblog.categorydata'),
            preserve_default=False,
        ),
    ]
