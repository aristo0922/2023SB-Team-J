# Generated by Django 3.2.20 on 2023-07-31 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_prometheus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('state', models.BooleanField(default=1)),
                ('is_selected', models.BooleanField(default=0)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('Image_upload'), models.Model),
        ),
        migrations.CreateModel(
            name='Ai_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('model_result_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('state', models.BooleanField(default=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('image_upload_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='image.image_upload')),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('Ai_model'), models.Model),
        ),
    ]
