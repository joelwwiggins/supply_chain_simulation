import pandas as pd

import streamlit as st

from streamlit_pandas_profiling import st_profile_report



st.write(
    """
# 📊 A/B Testing App
Upload your experiment results to see the significance of your A/B test.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

use_example_file = st.checkbox(
    "Use example file", False, help="Use in-built example file to demo the app"
)


vps5_crude_diet = pd.read_excel (r'C:\Users\jwiggins\Downloads\January 2017 Crude Diet Yields and Product Stream Quality.xlsx',sheet_name='VPS5 Crude Diet', header=[5]).iloc[1:,:]
vps5_yields = pd.read_excel (r'C:\Users\jwiggins\Downloads\January 2017 Crude Diet Yields and Product Stream Quality.xlsx',sheet_name='VPS5 Yields', header=[5]).iloc[1:,:]
vps5_strmq = pd.read_excel (r'C:\Users\jwiggins\Downloads\January 2017 Crude Diet Yields and Product Stream Quality.xlsx',sheet_name='VPS5 StrmQ', header=[6]).iloc[1:,:]

all_data=pd.concat([vps5_crude_diet,vps5_yields,vps5_strmq],axis=1)


pr = all_data.profile_report()

st_profile_report(pr)