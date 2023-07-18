# Generated by Django 4.2.3 on 2023-07-17 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0001_initial'),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_collage',
            name='img_origin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='image.image_origin'),
        ),
        migrations.AddField(
            model_name='image_collage',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image_chosen',
            name='img_origin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='image.image_origin'),
        ),
    ]
