import pickle 
import streamlit as st
import mysql.connector

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

def simpan_hasil_ke_database(hasil_klasifikasi):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Diabetes"
    )
    cursor = conn.cursor()

    sql = "INSERT INTO hasil_klasifikasi (Diabetes) VALUES (%s)"
    val = (hasil_klasifikasi,)
    cursor.execute(sql, val)

    conn.commit()
    conn.close()

#judul web
st.title('KLASIFIKASI POTENSI PENYAKIT DIABETES MELLITUS TIPE II PADA PASIEN MENGGUNAKAN ALGORITME NAÏVE BAYES GAUSSIAN')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Age = st.number_input('Input Nilai Age')
    hasil_klasifikasi = st.number_input('Hasil Klasifikasi')

with col2 :
    Gender = st.number_input('Input Nilai Gender')

with col1 :
    BMI = st.number_input('Input Nilai BMI')

with col2 :
    SBP = st.number_input('Input Nilai SBP (Systolic Blood Pressure)')

with col1 :
    DBP = st.number_input('Input Nilai DBP (Diastolic Blood Pressure)')

with col2 :
    FPG = st.number_input('Input Nilai FPG (Fasting Plasma Glucose)')
    
with col1 :
    Chol = st._input('Input Nilai Cholesterol')

with col2 :
    FFPG = st.text_input('Input Nilai FFPG (Final Fasting Plasma Glucose)')


#code untuk prediksi
diabetes_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diabetes_prediction = diabetes_model.predict([[Age, Gender, BMI, SBP, DBP, FPG, Chol, FFPG]])
    
    if(diabetes_prediction[0] == 0):
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabates'
    else:
        diabetes_diagnosis = 'Pasien Terkena Diabetes'   
         
    simpan_hasil_ke_database(hasil_klasifikasi)
    st.success(diabetes_diagnosis)

hasil_klasifikasi = st.selectbox("Hasil Klasifikasi", [0, 1])

if st.button("Simpan Hasil Klasifikasi"):
    simpan_hasil_ke_database(hasil_klasifikasi)
    st.success("Hasil Klasifikasi berhasil disimpan ke database.")