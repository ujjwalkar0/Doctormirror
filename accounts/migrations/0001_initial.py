# Generated by Django 3.0.6 on 2020-06-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ambulances',
            fields=[
                ('username', models.CharField(blank=True, max_length=20)),
                ('Driver_name', models.CharField(max_length=20)),
                ('Ambulances_Number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Hospital_Belongs_to', models.CharField(max_length=20)),
                ('Upload_Ambulance_Pic', models.ImageField(null=True, upload_to='Ambulance/')),
                ('Bed_to_Bed_Transfer_Facility', models.BooleanField(default=False)),
                ('emergency_online_support_team', models.BooleanField(default=False)),
                ('Special_care_teams_and_physicians', models.BooleanField(default=False)),
                ('Transfer_the_patient_under_doctors', models.BooleanField(default=False)),
                ('Both_side_road_ambulances', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=500)),
                ('collage', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('Passing_Year', models.CharField(max_length=500)),
                ('Experience', models.CharField(max_length=500)),
                ('Upload_Profile_Pic', models.FileField(blank=True, null=True, upload_to='dp/doctors/')),
                ('Degrees', models.CharField(max_length=500)),
                ('Supporting_Document', models.FileField(blank=True, null=True, upload_to='dp/doctors/')),
                ('Home_Address', models.CharField(max_length=500)),
                ('Your_Supporting_Document', models.FileField(blank=True, null=True, upload_to='dp/doctors/')),
                ('Hospital_or_Chamber_Address_1', models.CharField(max_length=500)),
                ('Hospital_or_Chamber_Address_2', models.CharField(blank=True, max_length=500)),
                ('Hospital_or_Chamber_Address_3', models.CharField(blank=True, max_length=500)),
                ('Hospital_or_Chamber_Address_4', models.CharField(blank=True, max_length=500)),
                ('Hospital_or_Chamber_Address_5', models.CharField(blank=True, max_length=500)),
                ('Specialist_of', models.CharField(default='0', max_length=500)),
                ('Kind_of_Treatment_Can_Do', models.CharField(blank=True, max_length=2)),
                ('fever', models.BooleanField(default=False)),
                ('dry_cough', models.BooleanField(default=False)),
                ('fatigue', models.BooleanField(default=False)),
                ('sputum_production', models.BooleanField(default=False)),
                ('shortness_of_breath', models.BooleanField(default=False)),
                ('mussle_or_joint_pain', models.BooleanField(default=False)),
                ('sore_throat', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('chills', models.BooleanField(default=False)),
                ('nausea_or_vomiting', models.BooleanField(default=False)),
                ('nasal_congestion', models.BooleanField(default=False)),
                ('diarrhoea', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('Hospital_Name', models.CharField(blank=True, max_length=120)),
                ('Address', models.CharField(blank=True, max_length=220)),
                ('Pictures', models.FileField(blank=True, null=True, upload_to='hospital/photos/')),
                ('Depertment', models.CharField(blank=True, max_length=20)),
                ('Microbiology', models.BooleanField(default=False)),
                ('Pathology', models.BooleanField(default=False)),
                ('Medicine', models.BooleanField(default=False)),
                ('Opthalmology', models.BooleanField(default=False)),
                ('Ostiology', models.BooleanField(default=False)),
                ('Sergery', models.BooleanField(default=False)),
                ('Features', models.CharField(blank=True, max_length=20)),
                ('Bypass_surgery', models.BooleanField(default=False)),
                ('Eye_operation', models.BooleanField(default=False)),
                ('Delivery', models.BooleanField(default=False)),
                ('Dialysis', models.BooleanField(default=False)),
                ('Anjioplasty', models.BooleanField(default=False)),
                ('Chemotherapy', models.BooleanField(default=False)),
                ('Dengue', models.BooleanField(default=False)),
                ('Covid_19_treatment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='nurses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=500)),
                ('collage', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=500)),
                ('Passing_Year', models.CharField(max_length=500)),
                ('Experience', models.CharField(max_length=500)),
                ('Upload_Profile_Pic', models.FileField(blank=True, null=True, upload_to='dp/nurses/')),
                ('Degrees', models.CharField(max_length=500)),
                ('Supporting_Document', models.FileField(blank=True, null=True, upload_to='dp/nurses/')),
                ('Home_Address', models.CharField(max_length=500)),
                ('Your_Supporting_Document', models.FileField(blank=True, null=True, upload_to='dp/nurses/')),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=500)),
                ('sugar', models.BooleanField(default=False)),
                ('Sugar_Report', models.FileField(blank=True, null=True, upload_to='patient_Report/')),
                ('pressure', models.BooleanField(default=False)),
                ('Presure_Report', models.FileField(blank=True, null=True, upload_to='patient_Report/')),
                ('heart', models.BooleanField(default=False)),
                ('Heart_Report', models.FileField(blank=True, null=True, upload_to='patient_Report/')),
                ('Any_Operation', models.BooleanField(default=False)),
                ('Report', models.FileField(blank=True, null=True, upload_to='patient_Report/')),
                ('Any_Other_Report', models.FileField(blank=True, null=True, upload_to='patient_Report/')),
            ],
        ),
        migrations.CreateModel(
            name='problems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=500)),
                ('fever', models.BooleanField(default=False)),
                ('dry_cough', models.BooleanField(default=False)),
                ('fatigue', models.BooleanField(default=False)),
                ('sputum_production', models.BooleanField(default=False)),
                ('shortness_of_breath', models.BooleanField(default=False)),
                ('mussle_or_joint_pain', models.BooleanField(default=False)),
                ('sore_throat', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('chills', models.BooleanField(default=False)),
                ('nausea_or_vomiting', models.BooleanField(default=False)),
                ('nasal_congestion', models.BooleanField(default=False)),
                ('diarrhoea', models.BooleanField(default=False)),
                ('others', models.CharField(blank=True, max_length=500)),
                ('File', models.FileField(blank=True, null=True, upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='usercatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('uses', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
