# Generated by Django 3.0.6 on 2020-06-09 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200610_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorresponse',
            name='abc',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]