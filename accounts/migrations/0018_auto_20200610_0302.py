# Generated by Django 3.0.6 on 2020-06-09 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_doctorresponse_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorresponse',
            old_name='messages',
            new_name='abc',
        ),
    ]
