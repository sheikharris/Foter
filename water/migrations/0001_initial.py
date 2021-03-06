# Generated by Django 3.0.3 on 2020-03-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_name', models.CharField(max_length=100)),
                ('contact_num1', models.CharField(max_length=13)),
                ('contact_num2', models.CharField(default=None, max_length=13)),
                ('crefititate_img1', models.ImageField(upload_to='pics')),
                ('crefititate_img2', models.ImageField(default=None, upload_to='pics')),
                ('distict', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('desc', models.TextField()),
                ('message', models.TextField()),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
