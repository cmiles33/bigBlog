# Generated by Django 4.0.1 on 2022-02-03 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0003_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=80)),
                ('likes', models.IntegerField(default=0)),
                ('disLikes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_data', to='mainblog.post')),
            ],
        ),
    ]
