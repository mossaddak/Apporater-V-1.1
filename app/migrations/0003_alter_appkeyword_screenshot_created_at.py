# Generated by Django 4.2 on 2023-04-26 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_campaign_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appkeyword_screenshot',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
