# Generated by Django 4.2.1 on 2023-05-23 19:56

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
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_star', models.IntegerField(default=0)),
                ('two_star', models.IntegerField(default=0)),
                ('three_star', models.IntegerField(default=0)),
                ('four_star', models.IntegerField(default=0)),
                ('five_star', models.IntegerField(default=0)),
                ('total_rate_count', models.IntegerField(default=0)),
                ('total_rate', models.IntegerField(default=0)),
                ('average_rate', models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='ecommerce.product')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
