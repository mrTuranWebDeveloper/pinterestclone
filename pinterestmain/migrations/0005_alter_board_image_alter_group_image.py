# Generated by Django 4.2 on 2023-08-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0004_alter_board_description_alter_group_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(upload_to='boards/'),
        ),
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(upload_to='groups/'),
        ),
    ]
