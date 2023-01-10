import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# Ovo je header
## Ovo je pod-header
Ovo je tekst""")

df = pd.DataFrame({
    'prva kolona': list(range(1, 11)),
    'druga kolona': np.arange(10, 101, 10)
})

st.checkbox("Čekiraj me")
# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Izaberite broj', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df