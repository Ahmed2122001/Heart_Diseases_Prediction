# Generated by Django 4.2.2 on 2023-06-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predict', '0006_remove_patient_username_patient_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patientname',
            new_name='patient_name',
        ),
        migrations.AlterField(
            model_name='patient',
            name='bp_meds',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cigarettes_per_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cp',
            field=models.IntegerField(blank=True, choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anginal Pain'), (4, 'Asymptomatic')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='diabetes',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='exang',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fbs',
            field=models.IntegerField(blank=True, choices=[(1, 'True'), (0, 'False')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='predict',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='patient',
            name='prevalent_hyp',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='prevalent_stroke',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='restecg',
            field=models.IntegerField(blank=True, choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Probable or Definite Left Ventricular Hypertrophy')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='slope',
            field=models.IntegerField(blank=True, choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Down Sloping')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='thal',
            field=models.IntegerField(blank=True, choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')], null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tot_chol',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
