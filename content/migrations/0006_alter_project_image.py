# Generated by Django 3.2.7 on 2021-09-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(blank=True, max_length=225, null=True),
        ),
    ]
