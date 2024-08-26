# Generated by Django 5.1 on 2024-08-25 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_item_back_coordinate_x_item_back_coordinate_y_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('sedan', 'Sedan'), ('suv', 'SUV'), ('truck', 'Truck')], default='sedan', max_length=100)),
                ('front_marked_image', models.CharField(blank=True, max_length=255, null=True)),
                ('front_before_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('front_after_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('front_after_top_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('left_marked_image', models.CharField(blank=True, max_length=255, null=True)),
                ('left_before_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('left_after_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('left_after_top_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('back_marked_image', models.CharField(blank=True, max_length=255, null=True)),
                ('back_before_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('back_after_base_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('back_after_top_coat', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]