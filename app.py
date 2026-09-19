import streamlit as st
import pandas as pd

st.set_page_config(page_title="داشبورد چهارسپرده", layout="wide")

st.title("📊 داشبورد هوشمند چهارسپرده ریالی")
st.write("فایل اکسل خود را بارگذاری کنید.")

uploaded_file = st.file_uploader("فایل اکسل را انتخاب کنید", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("داده‌های شما:")
    st.dataframe(df)
    st.success("فایل با موفقیت خوانده شد. آماده پردازش...")
