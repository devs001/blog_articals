# Generated by Django 3.0.7 on 2020-07-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0012_auto_20200715_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical_m',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
