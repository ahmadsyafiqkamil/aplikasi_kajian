# Generated by Django 4.1.8 on 2023-04-08 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('domain_id', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='domain_id')),
                ('domain_name', models.CharField(blank=True, max_length=250, null=True)),
                ('domain_url', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'tbl_domain',
            },
        ),
        migrations.CreateModel(
            name='KabDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.CharField(blank=True, max_length=4, null=True, verbose_name='domain_id')),
                ('domain_name', models.CharField(blank=True, max_length=250, null=True)),
                ('domain_url', models.CharField(blank=True, max_length=250, null=True)),
                ('domain_domain_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_economy.domain', verbose_name='domain dari domain')),
            ],
            options={
                'db_table': 'tbl_kab_domain',
            },
        ),
        migrations.CreateModel(
            name='AktifitasData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=256)),
                ('url', models.CharField(blank=True, max_length=256)),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(blank=True, null=True, verbose_name='updated')),
                ('data', models.JSONField(verbose_name='Data')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='updated by')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': '-created',
                'abstract': False,
            },
        ),
    ]