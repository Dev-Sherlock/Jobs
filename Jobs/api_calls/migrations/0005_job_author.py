# Generated by Django 3.2 on 2021-04-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_calls', '0004_auto_20210412_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]