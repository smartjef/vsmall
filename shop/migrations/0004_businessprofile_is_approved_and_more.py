# Generated by Django 4.0.8 on 2022-10-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_businessbranch_is_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]