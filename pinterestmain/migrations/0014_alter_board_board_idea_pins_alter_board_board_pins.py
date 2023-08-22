# Generated by Django 4.2 on 2023-08-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0013_board_board_idea_pins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_idea_pins',
            field=models.ManyToManyField(related_name='ideapin_boards', to='pinterestmain.ideapin'),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_pins',
            field=models.ManyToManyField(related_name='pin_boards', to='pinterestmain.pin'),
        ),
    ]
