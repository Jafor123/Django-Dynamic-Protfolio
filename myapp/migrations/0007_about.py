# Generated by Django 3.2.7 on 2021-10-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_service_work_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='About/')),
                ('details', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('career', models.CharField(max_length=11)),
            ],
        ),
    ]