# Generated by Django 4.2 on 2023-08-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0005_alter_board_image_alter_group_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_boards',
            field=models.ManyToManyField(blank=True, to='pinterestmain.board'),
        ),
    ]