# Generated by Django 5.0.3 on 2024-04-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0007_card_text_card_text_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='patronymic',
        ),
        migrations.AddField(
            model_name='card',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
