# Generated by Django 4.0.7 on 2022-10-22 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('profile_pic', django_resized.forms.ResizedImageField(blank=True, crop=None, default='uploads\\profile\\default.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 500], upload_to=users.models.content_file_name)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, max_length=300, null=True)),
                ('linked_in_link', models.URLField(blank=True, max_length=300, null=True)),
                ('facebook_link', models.URLField(blank=True, max_length=300, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('languages', models.ManyToManyField(blank=True, to='core.language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
