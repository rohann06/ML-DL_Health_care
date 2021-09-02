### ----Library-----

import streamlit as st
import pickle

### ----Data-----
heartmodel = pickle.load(open('Heart.pkl', 'rb'))
kidneymodel = pickle.load(open('Liver.pkl', 'rb'))
diabetesmodel = pickle.load(open('Diabetes.pkl', 'rb'))
breast_cancermodel = pickle.load(open('Breast_Cancer.pkl', 'rb'))

html = """<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/rohan-ahire-652001/" rel="nofollow"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/rohan-ahire-652001/" height="22" width="32""></a>
<a href="https://github.com/rohanA6" rel="nofollow"><img align="center" src="https://image.flaticon.com/icons/png/512/25/25231.png" alt="naz3eh" height="30" width="32" style="max-width:100%;"></a>
<a href="https://twitter.com/Rohan651" rel="nofollow"><img align="center" src="https://e1.pngegg.com/pngimages/589/288/png-clipart-clay-os-6-a-macos-icon-twitter-tweeter-icon-thumbnail.png" alt="Nazeeh_v21" height="35" width="35" style="max-width:100%;"></a>
</p>"""

footer = """<footer style="display: block;
    color: rgba(12, 0, 0, 0.4);
    flex: 0 1 0%;
    font-size: 0.8rem;
    max-width: 730px;
    padding: 4rem 4rem;
    width: 100%;">
    RohanAhire © 2021
</footer>"""

### ----Navigation-----
nav = st.sidebar.selectbox("Navigation Bar",
                           ['HomePage', 'Heart Disease', 'Liver Disease', 'Diabetes', 'Breast Cancer'],
                           )
cont = st.sidebar.markdown(html, unsafe_allow_html=True)

footer = st.sidebar.markdown(footer,unsafe_allow_html=True)
### ----Title----
st.title("ML HealthCare Project")

### -------------Home_Page------------

if nav == 'HomePage':
    html_temp = """
        <div style="background-color:#962D2D;padding:10px">
        <h2 style="margin:0px;padding:10px;color:white;text-align:center;font-size:3rem">Home Page</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown(
        '### **> This ML Healthcare project can helps you to detect someof the  disease from your body so you '
        'aware about your health .**')
    st.markdown(
        "### **>  This website contain some ML models to predict the result of the disease, the models this "
        "website contains are as bellow...**")

    st.write("")
    st.markdown("#### ⭕ Heart Disease Predictor")
    st.markdown("#### ⭕ Liver Disease Predictor")
    st.markdown("#### ⭕ Diabetes Predictor")
    st.markdown("#### ⭕ Breast Cancer Predictor")

    st.write("")
    st.title("1] Heart Disease")
    st.write("")
    st.image("heart.png")

    st.markdown(
        '### > Heart disease refers to any condition affecting the heart. There are many types, some of which are '
        'preventable. Unlike cardiovascular disease, which includes problems with the entire circulatory system, '
        'heart disease affects only the heart.')
    st.markdown("### **> Types of heart disease include:**")
    st.write("")
    st.write("")
    st.write("1] Arrhythmia. An arrhythmia is a heart rhythm abnormality.")
    st.write("2] Atherosclerosis. Atherosclerosis is a hardening of the arteries.")
    st.write("3] Cardiomyopathy. This condition causes the heart's muscles to harden or grow weak.")
    st.write("4] Congenital heart defects.")
    st.write("5] Coronary artery disease (CAD).")
    st.write("6] Heart infections.")

    st.write("")
    st.title("2] Liver Disease")
    st.write("")
    st.image("liver.jpeg")

    st.markdown(
        '### > The liver plays an important role in many bodily functions from protein production and blood clotting '
        'to cholesterol, glucose (sugar), and iron metabolism.Many diseases and conditions can affect the liver, '
        'for example, certain drugs like excessive amounts of acetaminophen, and acetaminophen combination '
        'medications like Vicodin and Norco, as well as statins, cirrhosis, alcohol abuse,hepatitis A, B, C, D, '
        'and E, infectious mononucleosis (Epstein Barr virus), nonalcoholic fatty liver disease (NASH), '
        'and iron overload (hemochromatosis).')

    st.markdown("### **> Liver Disease Symptoms & Signs:**")
    st.write("")
    st.write("")
    st.write("1] jaundice,")
    st.write("2] abdominal pain and swelling,")
    st.write("3] itchy skin,")
    st.write("4] dark urine color,")
    st.write("5] nausea,")
    st.write("6] vomiting,")
    st.write("7] chronic fatigue,")
    st.write("8] pale stool color,")
    st.write("9] bloody stool,")
    st.write("10]tar-colored stool,")
    st.write("11] loss of appetite,")

    st.write("")
    st.title("3] Diabetes Predictor")
    st.write("")
    st.image("diabetes.jpg")

    st.markdown(
        '### > Diabetes mellitus, commonly known as diabetes, is a metabolic disease that causes high blood sugar. '
        'The hormone insulin moves sugar from the blood into your cells to be stored or used for energy. With '
        'diabetes, your body either doesn’t make enough insulin or can’t effectively use the insulin it does make.')
    st.markdown('### > Untreated high blood sugar from diabetes can damage your nerves, eyes, kidneys, and other '
                'organs.')
    st.markdown("### **> Types of types of diabetes:**")
    st.write("")
    st.write("")
    st.write("1] Type 1 diabetes is an autoimmune disease. The immune system attacks and destroys cells in the "
             "pancreas, where insulin is made. It’s unclear what causes this attack. About 10 percent of people with "
             "diabetes have this type.")
    st.write(
        "2] Type 2 diabetes occurs when your body becomes resistant to insulin, and sugar builds up in your blood.")
    st.write("3] Prediabetes occurs when your blood sugar is higher than normal, but it’s not high enough for a "
             "diagnosis of type 2 diabetes.")
    st.write("4] Gestational diabetes is high blood sugar during pregnancy. Insulin-blocking hormones produced by the "
             "placenta cause this type of diabetes.")

    st.write("")
    st.title("5] Breast Cancer Predictor")
    st.write("")
    st.image("breast-cancer.jpg")

    st.markdown(
        "### > Breast cancer is cancer that forms in the cells of the breasts.After skin cancer, breast cancer is the "
        "most common cancer diagnosed in women in the United States. Breast cancer can occur in both men and women, "
        "but it's far more common in women.")
    st.markdown(
        '### > Substantial support for breast cancer awareness and research funding has helped created advances in '
        'the diagnosis and treatment of breast cancer. Breast cancer survival rates have increased, and the number of '
        'deaths associated with this disease is steadily declining, largely due to factors such as earlier detection, '
        'a new personalized approach to treatment and a better understanding of the disease.')
    st.markdown("### **> Types of types of diabetes:**")
    st.write("")
    st.write("")
    st.write("1] Angiosarcoma,")
    st.write("2] Ductal carcinoma in situ (DCIS),")
    st.write("3] Inflammatory breast cancer,")
    st.write("4] Lobular carcinoma in situ (LCIS),")
    st.write("5] Male breast cancer,")
    st.write("6] Paget's disease of the breast,")
    st.write("7] Recurrent breast cancer,")

    ### -------------Heart_Disease------------

if nav == 'Heart Disease':

    st.write("")
    ###Header
    html_temp = """
            <div style="background-color:#962D2D;padding:10px">
            <h2 style="margin:0px;padding:10px;color:white;text-align:center;font-size:3rem">Heart Disease</h2>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("")
    sex = st.selectbox('Enter Your Gender', ['Male', 'Female'])
    sex = 0 if sex == 'Female' else 1

    st.write("")
    age = st.number_input('Enter Your Age', min_value=1, step=1)

    st.write("")
    cp = st.selectbox('Enter Your chest pain type',
                      ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
    if cp == 'typical angina':
        cp = 0
    elif cp == 'atypical angina':
        cp = 1
    elif cp == 'non-anginal pain':
        cp = 2
    else:
        cp = 3

    st.write("")
    trestbps = st.number_input('Enter Your Resting Blood Pressure (in mm Hg on admission to the hospital)',
                               min_value=90, max_value=200)

    st.write("")
    chol = st.number_input('Enter Your Serum Cholestoral In mg/dl', min_value=120, max_value=570)

    st.write("")
    fbs = st.selectbox('Is Your Fasting Blood Sugar Is  > 120 mg/dl', ['Yes', 'No'])
    fbs = 0 if fbs == 'No' else 1

    st.write("")
    restecg = st.selectbox('Resting Electrocardiographic Results', ["normal",
                                                                    "having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)",
                                                                    "showing probable or definite left ventricular hypertrophy by Estes criteria"])
    if restecg == 'normal':
        restecg = 0
    elif restecg == 'having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)':
        restecg = 1
    else:
        restecg = 2

    st.write("")
    thalach = st.number_input('Maximum Heart Rate Achieved', min_value=70, max_value=205)

    st.write("")
    exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    exang = 0 if exang == 'No' else 1

    st.write("")
    oldpeak = st.number_input('ST Depression Induced By Exercise Relative To Rest', min_value=0.0, max_value=6.2)

    st.write("")
    slope = st.selectbox(' The Slope Of The Peak Exercise ST Segment', ['upsloping', 'flat', 'downsloping'])
    if slope == 'upsloping':
        slope = 0
    elif slope == 'flat':
        slope = 1
    else:
        slope = 2

    st.write("")
    ca = st.number_input('Number Of Major Vessels (0-3) Colored By Flourosopy', min_value=0, max_value=4, step=1)

    st.write("")
    thal = st.selectbox('Thal', ['normal', 'fixed_defect', 'reversable defect'])
    if thal == 'normal':
        thal = 1
    elif thal == 'fixed defect':
        thal = 2
    else:
        thal = 3

    st.write("")
    st.write("")

    if st.button("Predict"):
        try:
            result = heartmodel.predict(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if result == 0:
                st.success("Don't Worry! You Are Safe.........👍")
            else:
                st.error('Oops! Something Is Wrong With Your Body........😳')

        except:
            st.warning("Check The Inputs You've Entered....")

            ### -------------Liver------------

if nav == 'Liver Disease':

    st.write("")
    ###Header
    html_temp = """
                <div style="background-color:#962D2D;padding:10px">
                <h2 style="margin:0px;padding:10px;color:white;text-align:center;font-size:3rem">Liver Disease</h2>
                </div>
                """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("")
    Age = st.number_input("Enter Your Age", min_value=0)

    st.write("")
    Gender = st.selectbox("Gender", ['Male', 'Female'])
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    st.write("")
    Total_Bilirubin = st.number_input("Total_Bilirubin", min_value=0.0, step=0.1)

    st.write("")
    Direct_Bilirubin = st.number_input("Direct_Bilirubin", min_value=0.0, step=0.1)

    st.write("")
    Alkaline_Phosphotase = st.number_input("Alkaline_Phosphotase", min_value=0.0, step=0.1)

    st.write("")
    Alamine_Aminotransferase = st.number_input("Alamine_Aminotransferase", min_value=0.0, step=0.1)

    st.write("")
    Aspartate_Aminotransferase = st.number_input("Aspartate_Aminotransferase", min_value=0.0, step=0.1)

    st.write("")
    Total_Protiens = st.number_input("Total_Protiens", min_value=0.0, max_value=10.0, step=0.1)

    st.write("")
    Albumin = st.number_input("Albumin", min_value=0.0, max_value=6.0, step=0.1)

    st.write("")
    Albumin_and_Globulin_Ratio = st.number_input("Albumin_and_Globulin_Ratio", min_value=0.0, step=0.1)

    if st.button("Predict"):
        try:
            result = kidneymodel.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                                           Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens,
                                           Albumin, Albumin_and_Globulin_Ratio]])

            if result == 0:
                st.success("Don't Worry! You Are Safe.........👍")
            else:
                st.error('Oops! Something Is Wrong With Your Body........😳')

        except:
            st.warning("Check The Inputs You've Entered....")

            ### -------------Diabetes------------

if nav == 'Diabetes':

    st.write("")
    html_temp = """
        <div style="background-color:#962D2D;padding:10px">
        <h2 style="margin:0px;padding:10px;color:white;text-align:center;font-size:3rem">Diabetes</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("")
    Age = st.number_input("Age", min_value=1, step=1)

    st.write("")
    Pregnancies = st.number_input("Number Of Pregnancies", min_value=0, step=1)

    st.write("")
    Glucose = st.number_input("Level Of Glucose", min_value=20)

    st.write("")
    BloodPressure = st.number_input("Level Of BloodPressure", min_value=23)

    st.write("")
    SkinThickness = st.number_input("SkinThickness", min_value=10)

    st.write("")
    Insulin = st.number_input("Level Of Insulin", min_value=14)

    st.write("")
    BMI = st.number_input("BMI", min_value=18)

    st.write("")
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", min_value=0)

    if st.button("Predict"):
        try:
            result = diabetesmodel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                             BMI, DiabetesPedigreeFunction, Age]])

            if result == 0:
                st.success("Don't Worry! You Are Safe.........👍")
            else:
                st.error('Oops! Something Is Wrong With Your Body........😳')

        except:
            st.warning("Check The Inputs You've Entered....")

            ### -------------Breast Cancer------------

if nav == 'Breast Cancer':

    st.write("")
    html_temp = """
        <div style="background-color:#962D2D;padding:10px">
        <h2 style="margin:0px;padding:10px;color:white;text-align:center;font-size:3rem">Breast Cancer</h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.write("")
    radius_mean = st.number_input("radius_mean", min_value=0.0)

    st.write("")
    texture_mean = st.number_input("texture_mean", min_value=0.0, key='1')

    st.write("")
    smoothness_mean = st.number_input("smoothness_mean", min_value=0.0, key='2')

    st.write("")
    compactness_mean = st.number_input("compactness_mean", min_value=0.0, key='3')

    st.write("")
    concavity_mean = st.number_input("concavity_mean", min_value=0.0, key='4')

    st.write("")
    symmetry_mean = st.number_input("symmetry_mean", min_value=0.0, key='5')

    st.write("")
    fractal_dimension_mean = st.number_input("fractal_dimension_mean", min_value=0.0, key='6')

    st.write("")
    radius_se = st.number_input("radius_se", min_value=0.0)

    st.write("")
    texture_se = st.number_input("texture_se", min_value=0.0)

    st.write("")
    smoothness_se = st.number_input("smoothness_se", min_value=0.0)

    st.write("")
    compactness_se = st.number_input("compactness_se", min_value=0.0)

    st.write("")
    concavity_se = st.number_input("concavity_se", min_value=0.0)

    st.write("")
    concave_points_se = st.number_input("concave points_se", min_value=0.0)

    st.write("")
    symmetry_se = st.number_input("symmetry_se", min_value=0.0)

    st.write("")
    fractal_dimension_se = st.number_input("fractal_dimension_mean", min_value=0.0)

    st.write("")
    smoothness_worst = st.number_input("smoothness_worst", min_value=0.0)

    st.write("")
    compactness_worst = st.number_input("compactness_worst", min_value=0.0)

    st.write("")
    concavity_worst = st.number_input("concavity_worst ", min_value=0.0)

    st.write("")
    symmetry_worst = st.number_input("symmetry_worst", min_value=0.0)

    st.write("")
    fractal_dimension_worst = st.number_input("fractal_dimension_worst")

    if st.button("Predict"):
        try:
            result = breast_cancermodel.predict([[radius_mean, texture_mean, smoothness_mean, compactness_mean,
                                                  concavity_mean, symmetry_mean, fractal_dimension_mean, radius_se,
                                                  texture_se, smoothness_se, compactness_se, concavity_se,
                                                  concave_points_se, symmetry_se, fractal_dimension_se,
                                                  smoothness_worst, compactness_worst, concavity_worst, symmetry_worst,
                                                  fractal_dimension_worst]])

            if result == 1:
                st.error('Oops! Something Is Wrong With Your Body........😳')
            else:
                st.success("Don't Worry! You Are Safe.........👍")

        except:
            st.warning("Check The Inputs You've Entered....")

html = """<h3 align="left">Connect with me:</h3>
            <p align="left">
            <a href="https://linkedin.com/in/https://www.linkedin.com/in/rohan-ahire-652001/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/rohan-ahire-652001/" height="25" width="35" /></a>
            </p>
            <p align="left">
            <a href="https://github.com/rohanA6" target="blank"><img align="center" src="https://image.flaticon.com/icons/png/512/25/25231.png" height="32" width="35" /></a>
            </p>
            """


