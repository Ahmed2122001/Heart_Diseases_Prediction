# Generated by Django 4.2.2 on 2023-06-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('patientname', models.CharField(max_length=255)),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (0, 'Female')])),
                ('age', models.IntegerField()),
                ('current_smoker', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('cigarettes_per_day', models.IntegerField()),
                ('bp_meds', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('prevalent_stroke', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('prevalent_hyp', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('diabetes', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('tot_chol', models.IntegerField()),
                ('dia_bp', models.IntegerField()),
                ('sys_bp', models.IntegerField()),
                ('bmi', models.FloatField()),
                ('heart_rate', models.IntegerField()),
                ('glucose', models.IntegerField()),
                ('cp', models.IntegerField(choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anginal Pain'), (4, 'Asymptomatic')])),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField(choices=[(1, 'True'), (0, 'False')])),
                ('restecg', models.IntegerField(choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Probable or Definite Left Ventricular Hypertrophy')])),
                ('thalach', models.IntegerField()),
                ('oldpeak', models.FloatField()),
                ('slope', models.IntegerField(choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Down Sloping')])),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField(choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')])),
                ('exang', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('thal1', models.IntegerField(choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')])),
            ],
        ),
    ]
