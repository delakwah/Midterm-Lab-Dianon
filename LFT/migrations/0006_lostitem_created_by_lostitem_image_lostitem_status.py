# Generated by Django 5.1.4 on 2025-01-31 03:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LFT', '0005_remove_lostitem_created_by_remove_lostitem_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitem',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lostitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='status',
            field=models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], default='STATUS_CHOICES', max_length=20),
        ),
    ]
