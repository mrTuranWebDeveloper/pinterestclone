# Generated by Django 4.2 on 2023-09-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinterestmain', '0015_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_idea_pins',
            field=models.ManyToManyField(blank=True, related_name='ideapin_boards', to='pinterestmain.ideapin'),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_pins',
            field=models.ManyToManyField(blank=True, related_name='pin_boards', to='pinterestmain.pin'),
        ),
    ]
