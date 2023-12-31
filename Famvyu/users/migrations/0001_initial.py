# Generated by Django 4.2.6 on 2023-11-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_url', models.URLField(default='')),
                ('year', models.CharField(max_length=4)),
                ('duration', models.CharField(max_length=10)),
                ('star_rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('rate_count', models.CharField(blank=True, max_length=100, null=True)),
                ('product_url', models.URLField(default='')),
            ],
        ),
    ]
