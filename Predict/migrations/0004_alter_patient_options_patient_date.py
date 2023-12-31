# Generated by Django 4.2.2 on 2023-06-20 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Predict', '0003_alter_patient_current_smoker'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='patient',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
