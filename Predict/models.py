from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    SEX_CHOICES = (
        (1, 'Male'),
        (0, 'Female'),
    )
    SMOKER_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    BP_MEDS_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    STROKE_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    HYP_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    DIABETES_CHOICES = (
        (1, 'Yes'),
        (0, 'No'),
    )
    CP_CHOICES = (
        (1, 'Typical Angina'),
        (2, 'Atypical Angina'),
        (3, 'Non-Anginal Pain'),
        (4, 'Asymptomatic'),
    )
    FBS_CHOICES = (
        (1, 'True'),
        (0, 'False'),
    )
    RESTECG_CHOICES = (
        (0, 'Normal'),
        (1, 'ST-T Wave Abnormality'),
        (2, 'Probable or Definite Left Ventricular Hypertrophy'),
    )
    SLOPE_CHOICES = (
        (1, 'Upsloping'),
        (2, 'Flat'),
        (3, 'Down Sloping'),
    )
    THAL_CHOICES = (
        (3, 'Normal'),
        (6, 'Fixed Defect'),
        (7, 'Reversible Defect'),
    )
    THAL1_CHOICES = (
        (0, 'Normal'),
        (1, 'Fixed Defect'),
        (2, 'Reversible Defect'),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)
    sex = models.IntegerField(choices=SEX_CHOICES)
    age = models.IntegerField()
    current_smoker = models.IntegerField(choices=SMOKER_CHOICES, null=True, blank=True)
    cigarettes_per_day = models.IntegerField(null=True, blank=True)
    bp_meds = models.IntegerField(choices=BP_MEDS_CHOICES, null=True, blank=True)
    prevalent_stroke = models.IntegerField(choices=STROKE_CHOICES, null=True, blank=True)
    prevalent_hyp = models.IntegerField(choices=HYP_CHOICES, null=True, blank=True)
    diabetes = models.IntegerField(choices=DIABETES_CHOICES, null=True, blank=True)
    tot_chol = models.IntegerField(null=True, blank=True)
    dia_bp = models.IntegerField(null=True, blank=True)
    sys_bp = models.IntegerField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    glucose = models.IntegerField(null=True, blank=True)
    cp = models.IntegerField(choices=CP_CHOICES, null=True, blank=True)
    trestbps = models.IntegerField(null=True, blank=True)
    chol = models.IntegerField(null=True, blank=True)
    fbs = models.IntegerField(choices=FBS_CHOICES, null=True, blank=True)
    restecg = models.IntegerField(choices=RESTECG_CHOICES, null=True, blank=True)
    thalach = models.IntegerField(null=True, blank=True)
    oldpeak = models.FloatField(null=True, blank=True)
    slope = models.IntegerField(choices=SLOPE_CHOICES, null=True, blank=True)
    ca = models.IntegerField(null=True, blank=True)
    thal = models.IntegerField(choices=THAL_CHOICES, null=True, blank=True)
    exang = models.IntegerField(choices=SMOKER_CHOICES, null=True, blank=True)
    # thal1 = models.IntegerField(choices=THAL1_CHOICES)
    predict = models.CharField(max_length=500)
    date = models.DateTimeField(default= datetime.now)
    def __str__(self):
        return self.patient_name
    
    class Meta:
        ordering = ['-date']