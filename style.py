# ===============================
# style.py 
# ===============================

import streamlit as st


def load_style():

    st.markdown("""
    <style>

    /* ===============================
       MAIN BACKGROUND
    =============================== */
    .stApp{
        background: linear-gradient(
            135deg,
            #f7f8fa,
            #ffffff,
            #eef1f5
        );
    }

    /* ===============================
       CONTENT AREA
    =============================== */
    .block-container{
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;

        max-width: 1300px;
    }

    /* ===============================
       SIDEBAR
    =============================== */
    section[data-testid="stSidebar"]{
        background: #ffffff;
        border-right: 1px solid #ececec;
    }

    section[data-testid="stSidebar"] .stRadio > label{
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #111111;
    }

    div[role="radiogroup"] label{
        background: #ffffff;
        border: 1px solid #efefef;
        border-radius: 14px;
        padding: 10px;
        margin-bottom: 10px;
    }

    div[role="radiogroup"] label:hover{
        border: 1px solid #000000;
        transition: 0.2s;
    }

    div[role="radiogroup"] label p{
        font-size: 16px !important;
        font-weight: 600 !important;
    }

    /* ===============================
       TITLE
    =============================== */
    .main-title{
        background: white;
        padding: 28px;
        border-radius: 22px;
        border-left: 6px solid black;
        box-shadow: 0 10px 25px rgba(0,0,0,0.06);
        margin-bottom: 15px;

        font-size: 44px;
        font-weight: 800;
        line-height: 1.3;
        color: #111111;
    }

    .sub-title{
        background: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
        margin-bottom: 25px;

        font-size: 22px;
        font-weight: 700;
        color: #111111;
        line-height: 1.5;
    }

    /* ===============================
       BUTTON
    =============================== */
    .stButton > button{
        width: 100%;
        background: #000000;
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 18px;
        font-size: 16px;
        font-weight: 700;
    }

    .stButton > button:hover{
        background: #222222;
    }

    /* ===============================
       METRIC BOX
    =============================== */
    div[data-testid="metric-container"]{
        background: white;
        border: 1px solid #eeeeee;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 8px 18px rgba(0,0,0,0.04);
    }

    /* ===============================
       TABLE
    =============================== */
    .stDataFrame{
        border-radius: 14px;
        overflow: hidden;
    }

    /* ===============================
       FOOTER
    =============================== */
    footer{
        visibility: hidden;
    }

    </style>
    """, unsafe_allow_html=True)


def show_title():

    st.markdown("""
    <div class="main-title">
    🖥️ Development of a Web-Based System for Analyzing and Predicting Student Dropout Risk Using Machine Learning Techniques
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sub-title">
    🎓 การพัฒนาระบบเว็บไซต์เพื่อวิเคราะห์และทำนายความเสี่ยงการดรอปของนักศึกษาโดยใช้เทคนิคการเรียนรู้ของเครื่อง
    </div>
    """, unsafe_allow_html=True)