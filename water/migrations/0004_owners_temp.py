# Generated by Django 3.0.3 on 2020-03-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0003_auto_20200329_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='owners_temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_name', models.CharField(max_length=100)),
                ('contact_num1', models.CharField(max_length=13, unique=True)),
                ('contact_num2', models.CharField(default=None, max_length=13, unique=True)),
                ('crefititate_img1', models.ImageField(upload_to='pics')),
                ('crefititate_img2', models.ImageField(default=None, upload_to='pics')),
                ('distict', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('desc', models.TextField()),
                ('message', models.TextField()),
                ('amt_250', models.BooleanField(default=False)),
                ('img_250', models.ImageField(default=None, upload_to='pics')),
                ('amt_500', models.BooleanField(default=False)),
                ('img_500', models.ImageField(default=None, upload_to='pics')),
                ('amt_1000', models.BooleanField(default=False)),
                ('img_1000', models.ImageField(default=None, upload_to='pics')),
                ('amt_can', models.BooleanField(default=False)),
                ('img_can', models.ImageField(default=None, upload_to='pics')),
                ('des_can', models.TextField(default=None)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]