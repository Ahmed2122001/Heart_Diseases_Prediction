from django.urls import path
from . import views


urlpatterns=[
    path('Predict_4_Heart_Diseases',views.Predict_4_Heart_Diseases,name='Predict_4_Heart_Diseases'),
    path('Predict_Cardiovascular_Disease',views.Predict_Cardiovascular_Disease,name='Predict_Cardiovascular_Disease'),
    path('Predict_Coronary_Artery_Disease',views.Predict_Coronary_Artery_Disease,name='Predict_Coronary_Artery_Disease'),
    path('Predict_Heart_Attack',views.Predict_Heart_Attack,name='Predict_Heart_Attack'),
    path('Predict_Heart_Failure',views.Predict_Heart_Failure,name='Predict_Heart_Failure'),
    path('History',views.History,name='History')
]