# Generated by Django 4.1.4 on 2023-08-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_email', models.EmailField(max_length=50)),
                ('employee_phone', models.CharField(max_length=10)),
                ('employee_designation', models.CharField(max_length=50)),
                ('employee_department', models.CharField(max_length=50)),
                ('employee_salary', models.IntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='assets',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=50)),
                ('asset_type', models.CharField(max_length=50)),
                ('asset_condition', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='asset_assigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_checkout_date', models.DateField()),
                ('asset_return_date', models.DateField()),
                ('asset_log', models.CharField(max_length=200)),
                ('asset_assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker_app.employee')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
