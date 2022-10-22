# Generated by Django 4.0.7 on 2022-10-22 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_alter_product_branch_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
