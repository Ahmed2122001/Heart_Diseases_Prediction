document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();
  
    var sex = document.getElementById("sex").value;
    var age = document.getElementById("age").value;
    var currentSmoker = document.getElementById("current-smoker").value;
    var cigarettesPerDay = document.getElementById("cigarettes-per-day").value;
    var bpMeds = document.getElementById("bp-meds").value;
    var prevalentStroke = document.getElementById("prevalent-stroke").value;
    var prevalentHyp = document.getElementById("prevalent-hyp").value;
    var diabetes = document.getElementById("diabetes").value;
    var totChol = document.getElementById("tot-chol").value;
    var diaBp = document.getElementById("dia-bp").value;
    var sysBp = document.getElementById("sys-bp").value;
    var bmi = document.getElementById("bmi").value;
    var heartRate = document.getElementById("heart-rate").value;
    var glucose = document.getElementById("glucose").value;
    var cp = document.getElementById("cp").value;
    var trestbps = document.getElementById("trestbps").value;
    var chol = document.getElementById("chol").value;
    var fbs = document.getElementById("fbs").value;
    var restecg = document.getElementById("restecg").value;
    var thalach = document.getElementById("thalach").value;
    var oldpeak = document.getElementById("oldpeak").value;
    var slope = document.getElementById("slope").value;
    var ca = document.getElementById("ca").value;
    var thal = document.getElementById("thal").value;
  
    console.log("Sex:", sex);
    console.log("Age:", age);
    console.log("Current Smoker:", currentSmoker);
    console.log("Cigarettes Per Day:", cigarettesPerDay);
    console.log("BP Meds:", bpMeds);
    console.log("Prevalent Stroke:", prevalentStroke);
    console.log("Prevalent Hyp:", prevalentHyp);
    console.log("Diabetes:", diabetes);
    console.log("Tot Chol:", totChol);
    console.log("Dia BP:", diaBp);
    console.log("Sys BP:", sysBp);
    console.log("BMI:", bmi);
    console.log("Heart Rate:", heartRate);
    console.log("Glucose:", glucose);
    console.log("Chest Pain Type:", cp);
    console.log("Resting Blood Pressure:", trestbps);
    console.log("Serum Cholestoral:", chol);
    console.log("Fasting Blood Sugar:", fbs);
    console.log("Resting ECG Results:", restecg);
    console.log("Maximum Heart Rate Achieved:", thalach);
    console.log("ST Depression:", oldpeak);
    console.log("Slope of Peak Exercise ST Segment:", slope);
    console.log("Number of Major Vessels:", ca);
    console.log("Results of Nuclear Stress Test:", thal);



    var trestbps = document.getElementById("trestbps").value;
    var exang = document.getElementById("exang").value;
    // var thal1 = document.getElementById("thal1").value;

    console.log("Resting Blood Pressure:", trestbps);
    console.log("Exercise Induced Angina:", exang);
    // console.log("Thal:", thal1);
  });

  