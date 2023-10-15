# Generated by Django 3.2 on 2023-10-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_hotel', '0002_salary_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.CharField(default='', max_length=100)),
                ('contact', models.BigIntegerField()),
                ('salary', models.IntegerField()),
                ('join_date', models.DateField(null=True)),
                ('salary_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manage_hotel.salary_types')),
            ],
        ),
    ]
