# Generated by Django 4.2.2 on 2023-06-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predict', '0002_alter_patient_current_smoker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='current_smoker',
            field=models.IntegerField(blank=True, choices=[(1, 'Yes'), (0, 'No')], null=True),
        ),
    ]
