# Generated by Django 3.2 on 2023-10-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
