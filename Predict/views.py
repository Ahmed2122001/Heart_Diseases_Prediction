from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Patient
from django.contrib import auth
##############################
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# Create your views here.

def Predict_Cardiovascular_Disease_model(Cardiovascular_Disease_list):
    df_Cardiovascular=pd.read_csv('static\Dataset\Cardiovascular_Disease_dataset.csv')

    df_Cardiovascular['TenYearCHD'].value_counts(normalize = True)
    df_Cardiovascular['cigsPerDay'].value_counts(normalize = True).plot(kind="bar")
    df_Cardiovascular['cigsPerDay'][df_Cardiovascular['currentSmoker']==0].isna().sum()
    # creating a boolean array of smokers
    smoke = (df_Cardiovascular['currentSmoker']==1)
    # applying mean to NaNs in cigsPerDay but using a set of smokers only
    df_Cardiovascular.loc[smoke,'cigsPerDay'] = df_Cardiovascular.loc[smoke,'cigsPerDay'].fillna(df_Cardiovascular.loc[smoke,'cigsPerDay'].mean())
    df_Cardiovascular['cigsPerDay'][df_Cardiovascular['currentSmoker']==1].mean()
    df_Cardiovascular['cigsPerDay'][df_Cardiovascular['currentSmoker']==0].mean()
    df_Cardiovascular['education'].value_counts(normalize = True).plot(kind="bar")
    # Filling out missing values
    df_Cardiovascular['BPMeds'].fillna(0, inplace = True)
    df_Cardiovascular['glucose'].fillna(df_Cardiovascular.glucose.mean(), inplace = True)
    df_Cardiovascular['totChol'].fillna(df_Cardiovascular.totChol.mean(), inplace = True)
    df_Cardiovascular['education'].fillna(1, inplace = True)
    df_Cardiovascular['BMI'].fillna(df_Cardiovascular.BMI.mean(), inplace = True)
    df_Cardiovascular['heartRate'].fillna(df_Cardiovascular.heartRate.mean(), inplace = True)
    df_Cardiovascular.isna().sum()
    df_Cardiovascular = df_Cardiovascular.drop(['education'], axis = 1)
    # separate independent & dependent variables
    X_Cardiovascular = df_Cardiovascular.iloc[:,0:14]  #independent columns
    y_Cardiovascular = df_Cardiovascular.iloc[:,-1]    #target column i.e price range
    from imblearn.over_sampling import SMOTE
    smote = SMOTE(sampling_strategy='minority')
    X_sm_Cardiovascular, y_sm_Cardiovascular = smote.fit_resample(X_Cardiovascular, y_Cardiovascular)
    y_sm_Cardiovascular=pd.DataFrame(y_sm_Cardiovascular)
    y_sm_Cardiovascular.value_counts()
    from sklearn.model_selection import train_test_split
    X_train_Cardiovascular, X_test_Cardiovascular, y_train_Cardiovascular, y_test_Cardiovascular = train_test_split( X_sm_Cardiovascular,y_sm_Cardiovascular , test_size = 0.2, random_state = 0)
    print(X_train_Cardiovascular.shape)
    print(X_test_Cardiovascular.shape)
    y_train_Cardiovascular.value_counts()
    y_test_Cardiovascular.value_counts()
    # from sklearn.neighbors import KNeighborsClassifier


    knn_Cardiovascular = KNeighborsClassifier(n_neighbors=2)
    # Fit the model
    knn_Cardiovascular.fit(X_train_Cardiovascular,y_train_Cardiovascular)
    pred_Cardiovascular=knn_Cardiovascular.predict(X_test_Cardiovascular)

    test_accurac_Knn_Cardiovascular = accuracy_score(pred_Cardiovascular,y_test_Cardiovascular)
    
    
    Cardiovascular_Disease_list = [float(x) for x in Cardiovascular_Disease_list]
    Cardiovascular_Disease_list = np.array([Cardiovascular_Disease_list])
    predict_Cardiovascular = knn_Cardiovascular.predict(Cardiovascular_Disease_list)
    return  predict_Cardiovascular

def Predict_Coronary_Artery_Disease_model(Coronary_Artery_Disease_list):
    df_Coronary_Artery = pd.read_csv('static\Dataset\Coronary_Artery_dataset.csv',na_values = '?')
    df_Coronary_Artery['num'].replace({2:1, 3:1, 4:1}, inplace = True)
    df_Coronary_Artery['thal'].replace({3:1, 6:2, 7:3}, inplace = True)
    df_Coronary_Artery.dropna(how = 'any', inplace = True)


    y_Coronary_Artery = np.array(df_Coronary_Artery.iloc[:,-1:]) 
    X_Coronary_Artery = np.array(df_Coronary_Artery.iloc[:,:13]) 

    X_train_Coronary_Artery, X_test_Coronary_Artery, y_train_Coronary_Artery, y_test_Coronary_Artery = train_test_split(X_Coronary_Artery, y_Coronary_Artery, test_size=0.3, random_state=0)
    # RandomForestClassifier_Coronary_Artery = RandomForestClassifier(random_state = 10)
    # RandomForestClassifier_Coronary_Artery.fit(X_train_Coronary_Artery, y_train_Coronary_Artery)
    # y_pred_Coronary_Artery = RandomForestClassifier_Coronary_Artery.predict(X_test_Coronary_Artery)
    scaler = StandardScaler()
    X_train_Coronary_Artery_scaled = scaler.fit_transform(X_train_Coronary_Artery)
    X_test_Coronary_Artery_scaled = scaler.transform(X_test_Coronary_Artery)

    RandomForestClassifier_Coronary_Artery = RandomForestClassifier(random_state=10)
    RandomForestClassifier_Coronary_Artery.fit(X_train_Coronary_Artery_scaled, y_train_Coronary_Artery)

    y_pred_Coronary_Artery = RandomForestClassifier_Coronary_Artery.predict(X_test_Coronary_Artery_scaled)

    ##accuracy
    # accuracy_test_Coronary_Artery = accuracy_score(y_test_Coronary_Artery, y_pred_Coronary_Artery)
    # Store the input values in a list
    
    
    
    Coronary_Artery_Disease_list = [float(x) for x in Coronary_Artery_Disease_list]
    Coronary_Artery_Disease_list = np.array([Coronary_Artery_Disease_list])
    Coronary_Artery_Disease_list_scaled = scaler.fit_transform(Coronary_Artery_Disease_list)
    predict_Coronary_Artery = RandomForestClassifier_Coronary_Artery.predict(Coronary_Artery_Disease_list_scaled)
    return predict_Coronary_Artery
    
def Predict_Heart_Attack_model(Heart_Attack_list):
    df_Heart_Attack = pd.read_csv('static\Dataset\Heart_Attack_Analysis&Prediction_Dataset.csv')
    df_Heart_Attack.describe()
    labels_Heart_Attack= np.array(df_Heart_Attack.iloc[:,-1:])
    features_Heart_Attack= np.array(df_Heart_Attack.iloc[:,:13])
    # from sklearn.model_selection import train_test_split
    X_train_Heart_Attack, X_test_Heart_Attack, y_train_Heart_Attack, y_test_Heart_Attack = train_test_split(features_Heart_Attack, labels_Heart_Attack, test_size=0.3, random_state=0)
    scaler = StandardScaler()
    # transform data
    X_train_scaled_Heart_Attack = scaler.fit_transform(X_train_Heart_Attack)
    X_test_scaled_Heart_Attack = scaler.fit_transform(X_test_Heart_Attack)
    ##svm linear kernel
    # from sklearn.svm import SVC
    svm_linear_Heart_Attack = SVC(kernel='linear', C=100)
    svm_linear_Heart_Attack.fit(X_train_scaled_Heart_Attack, y_train_Heart_Attack)
    print("Accuracy:", svm_linear_Heart_Attack.score(X_train_scaled_Heart_Attack, y_train_Heart_Attack))
    print("Accuracy:", svm_linear_Heart_Attack.score(X_test_scaled_Heart_Attack, y_test_Heart_Attack))


    Heart_Attack_list = [float(x) for x in Heart_Attack_list]
    Heart_Attack_list = np.array([Heart_Attack_list])
    Heart_Attack_list_scaled = scaler.fit_transform(Heart_Attack_list)
    predict_Heart_Attack = svm_linear_Heart_Attack.predict(Heart_Attack_list_scaled)
    return predict_Heart_Attack

def Predict_Heart_Failure_model(Heart_Failure_list):
    df_Failure = pd.read_csv('static\Dataset\Heart_Failure_dataset.csv')
    df_Failure.describe()
    labels_Failure= np.array(df_Failure.iloc[:,-1:])
    features_Failure= np.array(df_Failure.iloc[:,:13])
    
    X_train_Failure, X_test_Failure, y_train_Failure, y_test_Failure = train_test_split(features_Failure, labels_Failure, test_size=0.3, random_state=0)
    
    # define min max scaler
    scaler = StandardScaler()
    # transform data
    X_train_scaled_Failure = scaler.fit_transform(X_train_Failure)
    X_test_scaled_Failure = scaler.fit_transform(X_test_Failure)
    # Polynomial Kernel
    svm_degree_4_Failure = SVC(kernel='poly', degree=4)
    svm_degree_4_Failure.fit(X_train_scaled_Failure, y_train_Failure)
    print("Polynomial kernel of degree = 4")
    print("Accuracy:", svm_degree_4_Failure.score(X_train_scaled_Failure, y_train_Failure))
    print("Accuracy:", svm_degree_4_Failure.score(X_test_scaled_Failure, y_test_Failure))

    Heart_Failure_list = [float(x) for x in Heart_Failure_list]
    Heart_Failure_list = np.array([Heart_Failure_list])
    Heart_Failure_list_scaled = scaler.fit_transform(Heart_Failure_list)
    predict_Heart_Failure = svm_degree_4_Failure.predict(Heart_Failure_list_scaled)
    return predict_Heart_Failure

def Predict_4_Heart_Diseases(request):
    if request.method == 'POST' and 'btnpredict' in request.POST:
        patient_name = request.POST.get('Patientname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        current_smoker = request.POST.get('current-smoker')
        cigarettes_per_day = request.POST.get('cigarettes-per-day')
        bp_meds = request.POST.get('bp-meds')
        prevalent_stroke = request.POST.get('prevalent-stroke')
        prevalent_hyp = request.POST.get('prevalent-hyp')
        diabetes = request.POST.get('diabetes')
        tot_chol = request.POST.get('tot-chol')
        dia_bp = request.POST.get('dia-bp')
        sys_bp = request.POST.get('sys-bp')
        bmi = request.POST.get('bmi')
        heart_rate = request.POST.get('heart-rate')
        glucose = request.POST.get('glucose')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        exang = request.POST.get('exang')
        thal = request.POST.get('thal')
        is_healthy = None
        # is_patient = None

        Cardiovascular_Disease_list = [sex, age,current_smoker, cigarettes_per_day, bp_meds, prevalent_stroke, prevalent_hyp, diabetes, tot_chol, sys_bp, dia_bp, bmi, heart_rate, glucose]
        Coronary_Artery_Disease_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,oldpeak, slope, ca, thal]
        Heart_Attack_list = [age,sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak, slope, ca, thal]
        Heart_Failure_list = [age,sex, cp, trestbps, chol, fbs, restecg, thalach, exang,oldpeak, slope, ca, thal]
        predict_Cardiovascular = Predict_Cardiovascular_Disease_model(Cardiovascular_Disease_list)
        predict_Coronary_Artery = Predict_Coronary_Artery_Disease_model(Coronary_Artery_Disease_list)
        predict_Heart_Attack = Predict_Heart_Attack_model(Heart_Attack_list)
        predict_Heart_Failure = Predict_Heart_Failure_model(Heart_Failure_list)


        if predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Cardiovascular or Coronary Artery or Heart Attack or Heart Failure'
            
            
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Cardiovascular or Coronary Artery or Heart Attack'
            
            
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Cardiovascular or Coronary Artery or Heart Failure'
           
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Cardiovascular or Coronary Artery'
           
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Cardiovascular or Heart Attack or Heart Failure'
           
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Cardiovascular or Heart Attack'
            
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Cardiovascular or Heart Failure'
        elif predict_Cardiovascular[0] == 1 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Cardiovascular'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Coronary Artery or Heart Attack or Heart Failure'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Coronary Artery or Heart Attack'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Coronary Artery or Heart Failure'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 1 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Coronary Artery'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Heart Attack or Heart Failure'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 1 and predict_Heart_Failure[0] == 0:
            predict = f'{patient_name} will have Heart Attack'
        elif predict_Cardiovascular[0] == 0 and predict_Coronary_Artery[0] == 0 and predict_Heart_Attack[0] == 0 and predict_Heart_Failure[0] == 1:
            predict = f'{patient_name} will have Heart Failure'
        else:
            predict = f'{patient_name} will  have not Heart Diseases'
            is_healthy = True
        

        user = request.user
        patient = Patient(user = user, 
                          patient_name = patient_name, 
                          sex = sex, 
                          age = age, 
                          current_smoker = current_smoker, 
                          cigarettes_per_day = cigarettes_per_day, 
                          bp_meds = bp_meds, 
                          prevalent_stroke = prevalent_stroke, 
                          prevalent_hyp = prevalent_hyp, 
                          diabetes = diabetes, 
                          tot_chol = tot_chol, 
                          sys_bp = sys_bp, 
                          dia_bp = dia_bp, 
                          bmi = bmi, 
                          heart_rate = heart_rate, 
                          glucose = glucose, 
                          cp = cp, 
                          trestbps = trestbps, 
                          chol = chol, 
                          fbs = fbs, 
                          restecg = restecg, 
                          thalach = thalach, 
                          oldpeak = oldpeak, 
                          slope = slope, 
                          ca = ca, 
                          thal = thal, 
                          exang = exang, 
                          predict = predict
                          )
        
        patient.save()
        if is_healthy == True:
            messages.success(request, predict)
        else:
            messages.error(request, predict)
        return redirect('Predict_4_Heart_Diseases')
    else:
        return render(request , 'Predict/Predict_4_Heart_Diseases.html')

def Predict_Cardiovascular_Disease(request):
    if request.method == 'POST' and 'btnpredict' in request.POST:
        # Cardiovascular_Disease_list = []
        patient_name = request.POST.get('Patientname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        current_smoker = request.POST.get('current-smoker')
        cigarettes_per_day = request.POST.get('cigarettes-per-day')
        bp_meds = request.POST.get('bp-meds')
        prevalent_stroke = request.POST.get('prevalent-stroke')
        prevalent_hyp = request.POST.get('prevalent-hyp')
        diabetes = request.POST.get('diabetes')
        tot_chol = request.POST.get('tot-chol')
        dia_bp = request.POST.get('dia-bp')
        sys_bp = request.POST.get('sys-bp')
        bmi = request.POST.get('bmi')
        heart_rate = request.POST.get('heart-rate')
        glucose = request.POST.get('glucose')

        
        
        Cardiovascular_Disease_list = [sex, age,current_smoker, cigarettes_per_day, bp_meds, prevalent_stroke, prevalent_hyp, diabetes, tot_chol, sys_bp, dia_bp, bmi, heart_rate, glucose]
        
        predict_Cardiovascular = Predict_Cardiovascular_Disease_model(Cardiovascular_Disease_list)
        
        if predict_Cardiovascular[0] == 0:
            predict = f'{patient_name} will not have Cardiovascular Disease'
            messages.success(request, predict)
        else:
            predict = f'{patient_name} will have Cardiovascular Disease'
            messages.error(request, predict)


        user = request.user
        patient = Patient(user = user, 
                          patient_name = patient_name, 
                          sex = sex, 
                          age = age, 
                          current_smoker = current_smoker, 
                          cigarettes_per_day = cigarettes_per_day, 
                          bp_meds = bp_meds, 
                          prevalent_stroke = prevalent_stroke, 
                          prevalent_hyp = prevalent_hyp, 
                          diabetes = diabetes, 
                          tot_chol = tot_chol, 
                          sys_bp = sys_bp, 
                          dia_bp = dia_bp, 
                          bmi = bmi, 
                          heart_rate = heart_rate, 
                          glucose = glucose, 
                          predict = predict
                          )
        
        patient.save()
        
        return redirect('Predict_Cardiovascular_Disease')
    else:
        return render(request , 'Predict/Predict_Cardiovascular_Disease.html')

def Predict_Coronary_Artery_Disease(request):
    if request.method == 'POST' and 'btnpredict' in request.POST:

        patient_name = request.POST.get('Patientname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')
        exang = int(request.POST.get('exang'))
        
        
        # Store the input values in a list
        Coronary_Artery_Disease_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,oldpeak, slope, ca, thal]
        
        
        
        predict_Coronary_Artery = Predict_Coronary_Artery_Disease_model(Coronary_Artery_Disease_list)
        
        if predict_Coronary_Artery[0] == 0:
            predict = f'You will not have Coronary Artery Disease'
            messages.success(request, predict)
        else:
            predict = f'You will have Coronary Artery Disease'
            messages.error(request, predict)
        

        user = request.user
        patient = Patient(user = user, 
                          patient_name = patient_name, 
                          sex = sex, 
                          age = age,  
                          cp = cp, 
                          trestbps = trestbps, 
                          chol = chol, 
                          fbs = fbs, 
                          restecg = restecg, 
                          thalach = thalach, 
                          oldpeak = oldpeak, 
                          slope = slope, 
                          ca = ca, 
                          thal = thal, 
                          exang = exang, 
                          predict = predict
                          )
        
        patient.save()

        return redirect('Predict_Coronary_Artery_Disease')
    else:
        return render(request , 'Predict/Predict_Coronary_Artery_Disease.html')

def Predict_Heart_Attack(request):
    if request.method == 'POST' and 'btnpredict' in request.POST:
        # patient_data = []

        patient_name = request.POST.get('Patientname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')
        exang = request.POST.get('exang')

        
        Heart_Attack_list = [age,sex, cp, trestbps, chol, fbs, restecg, thalach,exang,oldpeak, slope, ca, thal]
       
        predict_Heart_Attack = Predict_Heart_Attack_model(Heart_Attack_list)
        

        if predict_Heart_Attack[0] == 0:
            predict = f'You will not have Heart Attack Disease'
            messages.success(request, predict)
        else:
            predict = f'You will have Heart Attack Disease'
            messages.error(request, predict)


        user = request.user
        patient = Patient(user = user, 
                          patient_name = patient_name, 
                          sex = sex, 
                          age = age,  
                          cp = cp, 
                          trestbps = trestbps, 
                          chol = chol, 
                          fbs = fbs, 
                          restecg = restecg, 
                          thalach = thalach, 
                          oldpeak = oldpeak, 
                          slope = slope, 
                          ca = ca, 
                          thal = thal, 
                          exang = exang, 
                          predict = predict
                          )
        
        patient.save()

        return redirect('Predict_Heart_Attack')
    else:
        return render(request , 'Predict/Predict_Heart_Attack.html')

def Predict_Heart_Failure(request):
    if request.method == 'POST' and 'btnpredict' in request.POST:

        patient_name = request.POST.get('Patientname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')
        exang = request.POST.get('exang')
        
        
        Heart_Failure_list = [age,sex, cp, trestbps, chol, fbs, restecg, thalach, exang,oldpeak, slope, ca, thal]

        
        predict_Heart_Failure = Predict_Heart_Failure_model(Heart_Failure_list)
        

        if predict_Heart_Failure[0] == 0:
            predict = f'You will  have not Heart_Failure Disease'
            messages.success(request, predict)
        else:
            predict = f'You will have Heart Failure Disease'
            messages.error(request, predict)

        user = request.user
        patient = Patient(user = user, 
                          patient_name = patient_name, 
                          sex = sex, 
                          age = age,
                          cp = cp, 
                          trestbps = trestbps, 
                          chol = chol, 
                          fbs = fbs, 
                          restecg = restecg, 
                          thalach = thalach, 
                          oldpeak = oldpeak, 
                          slope = slope, 
                          ca = ca, 
                          thal = thal, 
                          exang = exang, 
                          predict = predict
                          )
        
        patient.save()
        
        
        return redirect('Predict_Heart_Failure')
    else:
        return render(request , 'Predict/Predict_Heart_Failure.html')

def History(request):


    context = None
    if request.user is not None:
        if not request.user.is_anonymous:
            user = request.user
            Patients = Patient.objects.filter(user=user)
            context={
                'patients': Patients
            }
        
        return render(request , 'Predict/History.html',context)
    
    else:
        redirect('History')