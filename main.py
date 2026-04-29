# ===============================
# main.py 
# ===============================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

from style import load_style, show_title
from model import train_model


# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# ===============================
# LOAD STYLE + TITLE
# ===============================
load_style()
show_title()

# ===============================
# LOAD MODEL
# ===============================
model, df, columns, X_test, y_test, accuracy, best_name, results = train_model()

# ===============================
# SIDEBAR
# ===============================
menu = st.sidebar.radio(
    "Menu | เมนู",
    [
        "Home | หน้าหลัก",
        "Dashboard | หน้าสรุปผล",
        "Prediction | หน้าทำนายผล",
        "Model Evaluation | ประเมินโมเดล"
    ]
)

# ==================================================
# HOME
# ==================================================
if menu == "Home | หน้าหลัก":

    st.markdown("## 🏠 Welcome | ยินดีต้อนรับ")

    st.info(
        "ระบบนี้ใช้ Machine Learning เพื่อวิเคราะห์ข้อมูลนักศึกษา "
        "และทำนายความเสี่ยงการดรอปของนักศึกษา"
    )

    st.success(
        "This system uses Machine Learning to analyze student data "
        "and predict dropout risk."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("📊 Dataset | ชุดข้อมูล", len(df))
    c2.metric("🤖 Best Model | โมเดลที่ดีที่สุด", best_name)
    c3.metric("🎯 Accuracy | ความแม่นยำ", f"{accuracy*100:.2f}%")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("📘 About Project | เกี่ยวกับโครงงาน")
        st.write(
            "ใช้ข้อมูล GPA, Attendance, สุขภาพจิต "
            "และปัจจัยอื่น ๆ เพื่อคาดการณ์ความเสี่ยงการดรอปของนักศึกษา"
        )
        st.caption("Use student data to predict dropout risk.")

    with right:
        st.subheader("⚙️ Workflow | ขั้นตอนการทำงาน")
        st.write("1. Collect Data | เก็บรวบรวมข้อมูล")
        st.write("2. Data Cleaning | ทำความสะอาดข้อมูล")
        st.write("3. Train Model | ฝึกโมเดล")
        st.write("4. Predict Risk | ทำนายความเสี่ยง")
        st.write("5. Decision Support | สนับสนุนการตัดสินใจ")


# ==================================================
# DASHBOARD
# ==================================================
elif menu == "Dashboard | หน้าสรุปผล":

    st.markdown("## 📊 Dashboard | หน้าสรุปผล")

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("📈 Dropout Distribution | การกระจายความเสี่ยง")
        st.bar_chart(df["dropout_risk"].value_counts())

    with c2:
        st.subheader("🥧 Risk Ratio | สัดส่วนความเสี่ยง")

        fig, ax = plt.subplots(figsize=(6, 4))
        df["dropout_risk"].value_counts().plot.pie(
            autopct="%1.1f%%",
            ax=ax
        )
        ax.set_ylabel("")
        st.pyplot(fig)

    st.markdown("---")

    st.subheader("📄 Sample Dataset | ตัวอย่างข้อมูล")
    st.dataframe(df.head(10), use_container_width=True)


# ==================================================
# PREDICTION
# ==================================================
elif menu == "Prediction | หน้าทำนายผล":

    st.markdown("## 🧪 Prediction System | ระบบทำนายผล")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender | เพศ", ["Male", "Female"])
        age = st.slider("Age | อายุ", 18, 30, 20)
        gpa = st.slider("GPA | เกรดเฉลี่ย", 1.0, 4.0, 3.0)
        attendance = st.slider(
            "Attendance Rate | อัตราการเข้าเรียน",
            0, 100, 80
        )
        study = st.slider(
            "Study Hours / Week | ชั่วโมงอ่านหนังสือ",
            0, 60, 15
        )

    with col2:
        financial = st.selectbox(
            "Financial Status | สถานะทางการเงิน",
            ["Low", "Medium", "High"]
        )

        scholarship = st.selectbox(
            "Scholarship | ทุนการศึกษา",
            ["Yes", "No"]
        )

        mental = st.slider(
            "Mental Health Score | คะแนนสุขภาพจิต",
            1, 10, 7
        )

        part_time = st.selectbox(
            "Part Time Job | งานพาร์ทไทม์",
            ["Yes", "No"]
        )

        family = st.selectbox(
            "Family Support | การสนับสนุนครอบครัว",
            ["Low", "Medium", "High"]
        )

    st.markdown("")

    if st.button(
        "🔍 Predict Result | ทำนายผล",
        use_container_width=True
    ):

        input_data = pd.DataFrame({
            "gender": [gender],
            "age": [age],
            "gpa": [gpa],
            "attendance_rate": [attendance],
            "study_hours_per_week": [study],
            "financial_status": [financial],
            "scholarship": [scholarship],
            "mental_health_score": [mental],
            "part_time_job": [part_time],
            "family_support": [family]
        })

        input_data = pd.get_dummies(input_data)
        input_data = input_data.reindex(
            columns=columns,
            fill_value=0
        )

        result = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0]

        low_prob = prob[0] * 100
        high_prob = prob[1] * 100

        st.markdown("---")

        if result == 1:
            st.error(
                f"⚠️ High Dropout Risk | มีความเสี่ยงสูง ({high_prob:.2f}%)"
            )
            st.warning("ควรได้รับการติดตามและดูแลเพิ่มเติม")

        else:
            st.success(
                f"✅ Low Dropout Risk | มีความเสี่ยงต่ำ ({low_prob:.2f}%)"
            )
            st.info("มีแนวโน้มเรียนต่อได้ตามปกติ")

        st.subheader("📊 Risk Probability | ความน่าจะเป็น")
        chart_df = pd.DataFrame({
            "Probability": [low_prob, high_prob]
        }, index=["Low Risk", "High Risk"])

        st.bar_chart(chart_df)


# ==================================================
# MODEL EVALUATION
# ==================================================
elif menu == "Model Evaluation | ประเมินโมเดล":

    st.markdown("## 📈 Model Evaluation | ประเมินประสิทธิภาพโมเดล")

    st.subheader("📊 Compare Models | เปรียบเทียบโมเดล")

    result_df = pd.DataFrame(
        results.items(),
        columns=["Model", "Accuracy"]
    )

    st.dataframe(result_df, use_container_width=True)

    st.subheader("📉 Accuracy Chart | กราฟเปรียบเทียบ")
    st.bar_chart(result_df.set_index("Model"))

    st.markdown("---")

    c1, c2 = st.columns(2)

    c1.metric(
        "🏆 Best Model | โมเดลที่ดีที่สุด",
        best_name
    )

    c2.metric(
        "🎯 Accuracy | ความแม่นยำ",
        f"{accuracy*100:.2f}%"
    )

    y_pred = model.predict(X_test)

    st.markdown("---")

    st.subheader("🧩 Confusion Matrix | ตารางความสับสน")

    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(6, 4))
    ConfusionMatrixDisplay(cm).plot(ax=ax)
    st.pyplot(fig)

    st.subheader("📄 Classification Report | รายงานผล")

    report = classification_report(
        y_test,
        y_pred,
        output_dict=True
    )

    report_df = pd.DataFrame(report).transpose()

    st.dataframe(report_df, use_container_width=True)


# ==================================================
# FOOTER
# ==================================================
st.markdown("---")

st.caption(
    "Bachelor Degree Project | โครงงานปริญญาตรี | "
    "Student Dropout Prediction System | ระบบทำนายการดรอปของนักศึกษา | 2026"
)