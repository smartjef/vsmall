# Generated by Django 4.0.8 on 2022-10-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_testimony_title_alter_team_photo'),
        ('shop', '0003_remove_businessbranch_address_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.RemoveField(
            model_name='businessprofile',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='latitude',
            field=models.DecimalField(decimal_places=16, default=-1.1139084362152138, max_digits=22),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='longitude',
            field=models.DecimalField(decimal_places=16, default=37.0106327842076, max_digits=22),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='core.tag'),
        ),
    ]