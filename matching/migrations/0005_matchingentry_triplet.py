# Generated by Django 3.1.4 on 2020-12-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0004_auto_20201221_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchingentry',
            name='triplet',
            field=models.BooleanField(default=True, help_text='Would you be okay with being matched in a triplet?'),
            preserve_default=False,
        ),
    ]
