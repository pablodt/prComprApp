# Generated by Django 3.2.6 on 2024-06-17 15:40

import api.models
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=api.models.generate_unique_code_house, max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuperMarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, related_name='purchasing_users', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='purchasing_users_permissions', to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=api.models.generate_unique_code_product, max_length=8, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('supermarket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.supermarket')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.purchasinguser')),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.purchasinguser'),
        ),
    ]
