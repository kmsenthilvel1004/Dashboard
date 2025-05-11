import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

st.title("Simple dta dashboard")

uploaded_file = st.file_uploader("Select file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Data summary")
    st.write(df.describe())

    st.subheader("Filtered Data")
    columns = df.columns.tolist()
    selected_colum = st.selectbox("Select colums to filterby",columns)
    unique_values = df[selected_colum].unique()
    selected_value = st.selectbox("Select Values",unique_values)

    filtered_value = df[df[selected_colum] == selected_value]

    st.write(filtered_value)
    st.subheader("Plot data")
    x = st.selectbox("Select X Axis",columns)
    y = st.selectbox("Select Y Axis",columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_value.set_index(x)[y])
else:
    st.write("Waiting for file upload")