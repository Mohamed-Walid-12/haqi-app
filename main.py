import streamlit as st

st.set_page_config(page_title="Haqi", layout="centered")
st.title("تطبيق حقي | Haqi App")

lang = st.selectbox("🌐 اختر اللغة / Select Language", ["العربية", "English"])

if lang == "العربية":
    st.markdown("### مرحبًا بك في تطبيق **حقي**")
    role = st.radio("أنت:", ["مستخدم", "محامي"])
    if role == "محامي":
        st.info("📌 البرنامج يأخذ عمولة 50 جنيه من كل خدمة تزيد عن 50 جنيه، و10٪ إذا كانت الخدمة تساوي أو تقل عن 50 جنيه.")
elif lang == "English":
    st.markdown("### Welcome to **Haqi App**")
    role = st.radio("You are:", ["User", "Lawyer"])
    if role == "Lawyer":
        st.info("📌 The app takes 50 EGP commission for services above 50 EGP, or 10% if 50 or below.")
